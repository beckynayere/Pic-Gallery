from django.shortcuts import render
rom django.http import HttpResponse,Http404,HttpRequest
from .models import Image,Location
import datetime as dt
# import sys  
# sys.setrecursionlimit(10000)


# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'gallery/index.html', {'images': images[::-1], 'locations': locations})

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'gallery/location.html', {'location_images': images})

def categories(request):
    categories = Category.objects.all()
    

    return render(request, 'categories.html', {"categories":categories})


 def category(request, id):

    try:
        category = Category.objects.get(id =id)
        images = Image.objects.get(category=category)
    except:
        raise Http404()

    return render(request,'category.html', {"category": category})



def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'gallery/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'gallery/search_results.html', {"message": message})

