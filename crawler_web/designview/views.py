from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from .forms import MainSearchForm
from django.views.generic import FormView, ListView
from django.views.generic.edit import FormMixin
from product.models import ProductModel, CarModel
from product.forms import ProductForm, ProductTopForm, CarTopForm
from django.db.models import Q
from decimal import Decimal


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


def select_search():

    sql_search = '''
       SELECT product_name, quantity
            FROM
            products
            ORDER BY quantity ASC LIMIT 100;
          '''
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_search)
            data = cursor.fetchall()
            columns = [column[0] for column in cursor.description]

    except ProgrammingError as ex:
        raise DatabaseError("Database query error - %s; query string - %s" % (
            ex, sql_search))

    return data


class ResultsPage(FormMixin, ListView):
    template_name = 'designview/results/results_page2.html'
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
                    'product': self.model.objects.filter(name__contains=name, )[:10],
                })
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            year = '0'
            website = []
            website1 = ''

            name = form.cleaned_data['car_name']
            year = form.cleaned_data['car_year']
            region = form.cleaned_data['region']
            # price_bottom = form.cleaned_data['price_bottom']
            # price_top = form.cleaned_data['price_top']

            print(year)
            # print(price_top)

            website = form.cleaned_data['website']

            if website:
                website1 = website[0]
            else:
                website1 = 'olx.uz'

            return render(
                request, self.template_name, {
                    'form': form,
                    'product': self.model.objects.filter(
                        Q(Q(car_year__gt=year) | Q(car_year__isnull=True))
                        & Q(car_name__contains=name) & Q(website__contains=website1)
                        & Q(region__contains=region)
                        # & Q(Q(car_year__gt=year) | Q(car_year__isnull=True))
                    )[:100],
                })

        return render(request, self.template_name, {'form': form})
