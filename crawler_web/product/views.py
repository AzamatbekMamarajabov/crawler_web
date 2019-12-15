from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import AccessMixin
from .models import ProductModel, CarModel
from .forms import ProductForm


from django.http import JsonResponse, HttpResponse
from rest_framework.generics import ListAPIView
from .serializers import CarSerializers
from .pagination import StandardResultsSetPagination


class CarListing(ListAPIView):
    # set the pagination and serializer class

    pagination_class = StandardResultsSetPagination
    serializer_class = CarSerializers

    def get_queryset(self):
        # filter the queryset based on the filters applied

        queryList = CarModel.objects.all()
        website = self.request.query_params.get('website', None)
        

        if website:
            queryList = queryList.filter(website=website)
        if variety:
            queryList = queryList.filter(variety=variety)
        if province:
            queryList = queryList.filter(province=province)
        if region:
            queryList = queryList.filter(region=region)

    # sort it if applied on based on price/points

        if sort_by == "price":
            queryList = queryList.order_by("price")
        elif sort_by == "points":
            queryList = queryList.order_by("points")
        return queryList


def getWebsites(request):
    # get all the countreis from the database excluding
    # null and blank values

    if request.method == "GET" and request.is_ajax():
        websites = CarModel.objects.exclude(website__isnull=True).\
            exclude(website__exact='').order_by(
                'website').values_list('website').distinct()
        websites = [i[0] for i in list(websites)]
        data = {
            "websites": websites,
        }
        return JsonResponse(data, status=200)
    
    

def getvariety(request):
    if request.method == "GET" and request.is_ajax():
        # get all the varities from the database excluding
        # null and blank values

        variety = Wine.objects.exclude(variety__isnull=True).\
            exclude(variety__exact='').order_by(
                'variety').values_list('variety').distinct()
        variety = [i[0] for i in list(variety)]
        data = {
            "variety": variety,
        }
        return JsonResponse(data, status=200)


def getProvince(request):
    # get the provinces for given country from the
    # database excluding null and blank values

    if request.method == "GET" and request.is_ajax():
        country = request.GET.get('country')
        province = Wine.objects.filter(country=country).\
            exclude(province__isnull=True).exclude(province__exact='').\
            order_by('province').values_list('province').distinct()
        province = [i[0] for i in list(province)]
        data = {
            "province": province,
        }
        return JsonResponse(data, status=200)


def getRegion(request):
    # get the regions for given province from the
    # database excluding null and blank values

    if request.method == "GET" and request.is_ajax():
        province = request.GET.get('province')
        region = Wine.objects.filter(province=province).\
            exclude(region__isnull=True).exclude(
                region__exact='').values_list('region').distinct()
        region = [i[0] for i in list(region)]
        data = {
            "region": region,
        }
        return JsonResponse(data, status=200)


##########################################################


class ProductListView(ListView):
    model = ProductModel
    queryset = ProductModel.objects.all()
    template_name = 'product/list.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = ProductModel
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        model = form.save(commit=False)
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = ProductModel
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product/detail.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'


class ProductUpdateView(UpdateView):
    model = ProductModel
    form_class = ProductForm
    template_name = 'product/update.html'
    success_url = reverse_lazy('product_list')
