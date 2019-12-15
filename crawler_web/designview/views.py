from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import MainSearchForm
from django.views.generic import FormView, ListView
from django.views.generic.edit import FormMixin
from product.models import ProductModel, CarModel
from product.forms import ProductForm, ProductTopForm, CarTopForm

class MainSearchPage(FormView):

    template_name = 'designview/search/search_page.html'
    form_class = MainSearchForm
    success_url = reverse_lazy('resultspage')

    def get(self, request, *args, **kwargs):

        if request.method == 'GET' and 'search_term' in request.GET:

            name = request.GET.get('search_term', '')

            form = self.form_class(request.GET)
           
            return render(
                request, reverse_lazy('resultspage'), {
                    'form': form, 
                    'name': name,
                })
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            
            return render(
                request, 'designview/results/results_page.html', {
                    'form': form, 
                    'name': name,
                })

        return render(request, 'designview/results/results_page.html', {'form': form})
    


class ResultsPage(FormMixin, ListView):
    template_name = 'designview/results/results_page.html'
    form_class = CarTopForm
    model = CarModel
    success_url = reverse_lazy('resultspage')
    paginate_by = 10

    def get(self, request, *args, **kwargs):

        if request.method == 'GET' and 'car_name' in request.GET:

            name = request.GET.get('car_name', '')
            print(name)

            form = self.form_class(request.GET)


            return render(
                request, self.template_name, {
                    'form': form, 
                    'product': self.model.objects.filter(name__contains=name)[:10],
                })
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['car_name']
            
            print(name)
            return render(
                request, self.template_name, {
                    'form': form, 
                    'product': self.model.objects.filter(car_name__contains=name)[:10],
                })

        return render(request, self.template_name, {'form': form})
    