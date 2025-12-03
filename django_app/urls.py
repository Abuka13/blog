from django.urls import path

from django_app import views
urlpatterns = [
    path("main/", views.main, name="main"),
    path("posts/", views.get_posts, name="posts"),
    path("posts/<int:pk>/", views.post_detail, name="post_detail")
]