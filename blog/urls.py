from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("archives/", views.archives, name="archives"),
    path("categories/", views.categories, name="categories"),
    path("tags/", views.tags, name="tags"),
    path("categories/<str:slug>/", views.category_detail, name="category_detail"),
    path("tags/<str:slug>/", views.tag_detail, name="tag_detail"),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]
