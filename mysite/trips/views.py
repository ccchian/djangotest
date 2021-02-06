# from django.shortcuts import render
# from django.http import HttpResponse


# def hello_world(request):
#     return HttpResponse("Hello World!")
# # Create your views here.
from datetime import datetime
from django.shortcuts import render
from .models import Post


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
    
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
#hello_world沒有在範例裡