
from django.urls import path, re_path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('error/', views.MainSearchPage.as_view(), name='main_searchpage'),
    re_path('', views.ResultsPage.as_view(), name='resultspage'),

    #re_path('product/', include("product.urls")),
]
