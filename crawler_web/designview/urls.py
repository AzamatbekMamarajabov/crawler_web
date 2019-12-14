
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MainSearchPage.as_view(), name='main_searchpage'),
    path('results/', views.ResultsPage, name='resultspage'),
]
