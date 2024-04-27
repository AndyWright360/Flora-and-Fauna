from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Range


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    products = Product.objects.all()
    query = None
    category = None
    range = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            if category:
                products = products.filter(category=category)
        
        if 'range' in request.GET:
            range = request.GET['range']
            products = products.filter(range__name=range)
            range = Range.objects.filter(name=range)

        if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('products'))
                
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'category': category,
        'range': range,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)