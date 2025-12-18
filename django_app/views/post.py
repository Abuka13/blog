from django.shortcuts import render, redirect
from django.urls import reverse
from django_app.forms import PostForm
from django_app import models
from django.core.paginator import Paginator


def get_posts(request):
    if request.method == "GET":
        posts = models.Post.objects.all().order_by('created_at')
        selected_page = request.GET.get(key="page", default = 1)
        limit_post_by_page = 3
        paginator = Paginator(posts, limit_post_by_page)
        current_page = paginator.get_page(selected_page)
        return render(request, 'posts/get_posts.html',  context={"current_page": current_page})

def post_detail(request, pk):
    post = models.Post.objects.get(id=pk)
    return render(request, 'posts/post_detail.html', context={"post":post})

def post_form(request):
    form = PostForm()
    if request.method == "GET":
        form = PostForm()
        return render(request, 'posts/post_form.html', {"form": form})
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse(get_posts))
    return render(
        request,
        "posts/post_form.html",
        {"form": form}
    )

