from django.shortcuts import render
import datetime as dt

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'gallery/index.html', {'images': images[::-1], 'locations': locations})
