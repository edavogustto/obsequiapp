from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Client, Product
from .forms import ClientForm, ProductForm

# Create your views here.

def index(request):

    return render(request, 'base.html')

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_create.html'
    success_url = ''  # Replace 'success_url' with the URL to redirect after successful form submission

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')
