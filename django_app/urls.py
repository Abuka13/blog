from django.urls import path

from django_app import views
urlpatterns = [
    path("main/", views.main, name="main"),


    ##TODO POSTS
    path("posts/", views.get_posts, name="posts"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail"),
    path("posts/create/", views.post_form, name="post_form")
]