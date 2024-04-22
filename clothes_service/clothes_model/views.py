from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from djongo.models import Q
from .models import Clothes, ClothesCategory
from .serializers import ClothesSerializer, ClothesCategorySerializer

class ClothesViewSet(viewsets.ModelViewSet):
	queryset = Clothes.objects.all()
	serializer_class = ClothesSerializer
	@action(detail=False, methods=['get'], url_path='search/(?P<keyword>[^/.]+)')
	def search(self, request, keyword=''):
		words = keyword.split()
		# Thực hiện truy vấn MongoDB để lấy các sản phẩm phù hợp
		clothes = Clothes.objects.filter(
			Q(name__icontains=words[0]) |
			Q(brand__icontains=words[0]) |
			Q(meta_keyword__icontains=words[0])
		)
		for word in words[1:]:
			clothes = clothes.filter(
				Q(name__icontains=word) |
				Q(brand__icontains=word) |
				Q(meta_keyword__icontains=word)
			)
		serializer = ClothesSerializer(clothes, many=True)
		return Response(serializer.data)
		
	
class ClothesCategoryViewSet(viewsets.ModelViewSet):
	queryset = ClothesCategory.objects.all()
	serializer_class = ClothesCategorySerializer