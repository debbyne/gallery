# from turtle import title
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images

# Create your views here.
def index(request):
    images = Images.get_images()
    title= 'Thee Dev Gallery'
    return render(request, 'all-photos/pictures.html', {"images":images, "title":title})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Images.search_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
