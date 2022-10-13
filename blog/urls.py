from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="home"),
    path("categories/", views.categories, name="categories"),
    path("tags/", views.tags, name="tags"),
    path("archives/", views.archives, name="archives"),
    path("about/", views.about, name="about"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]
