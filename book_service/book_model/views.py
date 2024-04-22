from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from djongo.models import Q
from .models import Book, BookCategory
from .serializers import BookSerializer, BookCategorySerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	@action(detail=False, methods=['post'], url_path='search/(?P<keyword>[^/.]+)')
	def search(self, request, keyword=''):
		words = keyword.split()
		# Thực hiện truy vấn MongoDB để lấy các sản phẩm phù hợp
		books = Book.objects.filter(
			Q(name__icontains=words[0]) |
			Q(brand__icontains=words[0]) |
			Q(meta_keyword__icontains=words[0])
		)
		for word in words[1:]:
			books = books.filter(
				Q(name__icontains=word) |
				Q(brand__icontains=word) |
				Q(meta_keyword__icontains=word)
			)
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)
		
	
class BookCategoryViewSet(viewsets.ModelViewSet):
	queryset = BookCategory.objects.all()
	serializer_class = BookCategorySerializer