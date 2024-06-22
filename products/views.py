from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User

from .models import Product, Range
from .forms import ProductForm
from wishlist.models import WishlistItem
from reviews.models import Review


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
    reviews = Review.objects.filter(product=product)
    other_products_in_range = Product.objects.filter(range=product.range).exclude(pk=product_id)
    
    if request.user.is_authenticated:
        product_in_wishlist = WishlistItem.objects.filter(product=product, user=request.user).exists()
    else:
        product_in_wishlist = False
    
    context = {
        'product': product,
        'reviews': reviews,
        'product_in_wishlist': product_in_wishlist,
        'other_products_in_range': other_products_in_range,
    }
    
    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))