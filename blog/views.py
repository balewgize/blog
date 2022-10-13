from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def post_detail(request, slug="post-slug-will-be-passed-from-url"):
    return HttpResponse("Post detail")


def categories(request):
    return HttpResponse("Categories page")


def tags(request):
    return HttpResponse("Tags page")


def archives(request):
    return HttpResponse("Archives page")


def about(request):
    return HttpResponse("About page")
