from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
from django.views import View

from django.shortcuts import render
from .utils import get_price_ranked_products

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

from rest_framework.permissions import IsAuthenticated



# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, Django Bootcamp!")

class APIView(View):
    def get(self, request):
        data = {
            "message": "Welcome to Django Bootcamp API!",
            "status": "success"
        }
        return JsonResponse(data)


class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'core/post_list.html', {'posts': posts})
    

class RankedProductsView(View):
    def get(self, request):
        ranked_products = get_price_ranked_products()
        return render(request, 'core/ranked_products.html', {'ranked': ranked_products})
    

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]