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
from rest_framework import generics
from .permissions import IsAdminOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsManager

# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, Django Bootcamp!")

class WelcomeAPIView(View):
    def get(self, request):
        data = {
            "message": "Message from feature branch",
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
    permission_classes = [IsAdminOrReadOnly]



class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]



class ManagerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsManager]

    def get(self, request):
        return Response({"message": "Hello Manager!"})