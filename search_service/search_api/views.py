import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class SearchAPIView(APIView):
    def get(self, request):  
        query = request.query_params.get('query')
        if query:
            # Gửi yêu cầu đến các dự án khác 'http://127.0.0.1:8003/search/?query=iphone'
            book_results = requests.get('http://127.0.0.1:8003/books/search/{}'.format(query)).json()
            clothes_results = requests.get('http://127.0.0.1:8001/clothes/search/{}'.format(query)).json()
            mobile_results = requests.get('http://127.0.0.1:8002/mobiles/search/{}'.format(query)).json()
        else:
            # Nếu từ khóa trống, lấy tất cả sản phẩm từ các dự án khác
            book_results = requests.get('http://127.0.0.1:8003/books/').json()
            clothes_results = requests.get('http://127.0.0.1:8001/clothes/').json()
            mobile_results = requests.get('http://127.0.0.1:8002/mobiles/').json()

        # Kết hợp kết quả từ các dự án khác
        combined_results = {
            'books': book_results,
            'clothes': clothes_results,
            'mobiles': mobile_results
        }
        
        # Trả về kết quả kết hợp
        return Response(combined_results)
