
from django.urls import path, re_path, include
from django.conf.urls import url
from . import views



urlpatterns = [
    path('', views.MainSearchPage.as_view(), name='main_searchpage'),
    re_path('results/' ,views.ResultsPage.as_view(), name='resultspage'),

    #re_path('product/', include("product.urls")),
]
