
from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Product, Customer

# Create your views here.

def home(request):
    return render(request, 'plp_ecommerce/home.html')

def product_list(request):
    # This is a view created
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request,'plp_ecommerce/product_list.html',context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product' : product,
    }
    return render(request, 'plp_ecommerce/product_detail.html', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers' : customers
    }
    return render(request, 'plp_ecommerce/customer_list.html', context)

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {
        'customer' : customer,
    }
    return render(request, 'plp_ecommerce/customer_detail.html', context)