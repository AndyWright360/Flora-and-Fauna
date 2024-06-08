from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from .models import Product, Range
from wishlist.models import WishlistItem


def all_products(request):
    """
    A view to show all products, including sorting & searching
    """

    products = Product.objects.all()
    query = None
    category = None
    range = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'range':
                sortkey = 'range__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    # Check if each product is in the user's wishlist
    user_wishlist = []
    if request.user.is_authenticated:
        user_wishlist = list(WishlistItem.objects.filter(user=request.user).values_list('product_id', flat=True))

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'category': category,
        'range': range,
        'current_sorting': current_sorting,
        'user_wishlist': user_wishlist,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, id=product_id)
    
    if request.user.is_authenticated:
        product_in_wishlist = WishlistItem.objects.filter(product=product, user=request.user).exists()
    else:
        product_in_wishlist = False
    
    context = {
        'product': product,
        'product_in_wishlist': product_in_wishlist,
    }
    
    return render(request, 'products/product_detail.html', context)