# from turtle import title
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images

# Create your views here.
def index(request):
    images = Images.objects.all()
    title= 'Thee Dev Gallery'
    return HttpResponse(request, {"images":images, "title":title})