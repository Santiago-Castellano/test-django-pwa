from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def index_two(request):
    return render(request, "index_two.html")

def index_tree(request):
    return render(request, "index_tree.html")
