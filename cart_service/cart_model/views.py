from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Cart
from .serializers import CartSerializer
import requests

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serialized_data = []
        for item in queryset : 
            product_id = item.product_id
            product_info = self.get_product_info(product_id)
            if product_info:
                item_data = CartSerializer(item).data
                item_data['product'] = product_info
                serialized_data.append(item_data)
        return Response(serialized_data)

    def get_product_info(self, product_id):
        #xác định dvu sp từ product_id
        product_id_num = product_id.split('_')[1]
        
        service = None
        if 'book' in product_id:
            service = 'books'
        elif 'clothes' in product_id:
            service = 'clothes'
        elif 'mobile' in product_id:
            service = 'mobiles'
        
        if service:
            #Xây dụng URL dựa trên dịch vụ sp và product_id
            port_map = {'books': 8003, 'clothes': 8001, 'mobiles': 8002}
            port = port_map.get(service)
            if port:
                url = f"http://127.0.0.1:{port}/{service}/{product_id_num}"
                print(url)
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        return response.json()
                except requests.RequestException as e:
                    pass
        return None

    @action(detail=False, methods=['get'], url_path='cart_by_user/(?P<user_id>[^/.]+)')
    def cart_by_user(self, request, user_id):
        cart = Cart.objects.filter(user_id=user_id)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
