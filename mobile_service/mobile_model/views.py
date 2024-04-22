from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from djongo.models import Q
from .models import Mobile, MobileCategory
from .serializers import MobileSerializer, MobileCategorySerializer

class MobileViewSet(viewsets.ModelViewSet):
	queryset = Mobile.objects.all()
	serializer_class = MobileSerializer
	@action(detail=False, methods=['get'], url_path='search/(?P<keyword>[^/.]+)')
	def search(self, request, keyword=''):
		words = keyword.split()
		# Thực hiện truy vấn MongoDB để lấy các sản phẩm phù hợp
		mobiles = Mobile.objects.filter(
			Q(name__icontains=words[0]) |
			Q(brand__icontains=words[0]) |
			Q(meta_keyword__icontains=words[0])
		)
		for word in words[1:]:
			mobiles = mobiles.filter(
				Q(name__icontains=word) |
				Q(brand__icontains=word) |
				Q(meta_keyword__icontains=word)
			)
		serializer = MobileSerializer(mobiles, many=True)
		return Response(serializer.data)
		
	
class MobileCategoryViewSet(viewsets.ModelViewSet):
	queryset = MobileCategory.objects.all()
	serializer_class = MobileCategorySerializer