from django.shortcuts import render
from .forms import MainSearchForm
from django.views.generic import FormView

class MainSearchPage(FormView):

    template_name = 'search/search_page.html'
    form_class = MainSearchForm
    success_url = '/thanks/'


class ResultsPage():
    pass
