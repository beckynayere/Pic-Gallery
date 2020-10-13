from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='galery'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^category/(\d+)', views.category, name='category'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)