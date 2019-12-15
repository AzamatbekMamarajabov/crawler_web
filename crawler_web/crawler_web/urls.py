
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('designview.urls')),
    re_path('product/', include(('product.urls', 'product'), namespace='product')),
    
]
