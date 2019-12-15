from django.urls import path, re_path

from .views import *


urlpatterns = [

     path('product_listing/', CarListing.as_view(), name = 'listing'),
     path("ajax/websites/", getWebsites, name = 'get_websites'),
     path("ajax/variety/", getvariety, name = 'get_varieties'),
     path("ajax/province/", getProvince, name = 'get_provinces'),
     path("ajax/region/", getRegion, name = 'get_regions'),
]
