from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import AccessMixin
from .models import ProductModel
from .forms import ProductForm

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

