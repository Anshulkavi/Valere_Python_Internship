from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import ListView, DetailView
# Create your views here.

class CategoryListView(ListView):
    model = Category
    template_name = "ecom_online/category_list.html"
    context_object_name = "categories"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "ecom_online/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=self.object)
        return context
        

# List all products
class ProductListView(ListView):
    model = Product
    template_name = "ecom_online/product_list.html"
    context_object_name = "products"
    ordering = ["-created_at"]

# Show a single product detail
class ProductDetailView(DetailView):
    model  = Product
    template_name = "ecom_online/product_detail.html"
    context_object_name = "product"