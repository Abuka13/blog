from django.shortcuts import render
from django_app import models



def get_posts(request):
    if request.method == "GET":
        posts = models.Post.objects.all().order_by('-created_at')
        return render(request, 'posts/get_posts.html',  context={"posts": posts})

def post_detail(request, pk):
    post = models.Post.objects.get(id=pk)
    return render(request, 'posts/post_detail.html', context={"post":post})