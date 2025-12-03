from django.shortcuts import render
from django_app import models
from django.core.paginator import Paginator


def get_posts(request):
    if request.method == "GET":
        posts = models.Post.objects.all().order_by('-created_at')
        selected_page = request.GET.get(key="page", default = 1)
        limit_post_by_page = 3
        paginator = Paginator(posts, limit_post_by_page)
        current_page = paginator.get_page(selected_page)
        return render(request, 'posts/get_posts.html',  context={"current_page": current_page})

def post_detail(request, pk):
    post = models.Post.objects.get(id=pk)
    return render(request, 'posts/post_detail.html', context={"post":post})


