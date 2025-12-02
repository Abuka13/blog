from django.urls import path

from django_app import views
urlpatterns = [
    path("home/", views.home, name="home"),
    path("posts/", views.get_posts, name="posts"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail")
]