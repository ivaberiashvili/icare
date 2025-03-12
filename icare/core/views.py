from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Post
from django.views import View


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