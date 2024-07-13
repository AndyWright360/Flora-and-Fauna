from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

from .models import WishlistItem
from products.models import Product


@login_required()
def add_to_wishlist(request):
    product_id = request.GET['id']
    product = Product.objects.get(id=product_id)

    context = {}

    wishlist_count = WishlistItem.objects.filter(
        product=product, user=request.user).count()

    if wishlist_count > 0:
        context = {
            "bool": True
        }
    else:
        new_wishlist = WishlistItem.objects.create(
            product=product,
            user=request.user
        )
        context = {
                "bool": True
            }

    return JsonResponse(context)


@login_required()
def remove_from_wishlist(request):
    product_id = request.GET.get('id')
    wishlist_item = WishlistItem.objects.filter(
        user=request.user, product_id=product_id).first()

    if wishlist_item:
        wishlist_item.delete()
        context = {"bool": True}
    else:
        context = {"bool": False}

    return JsonResponse(context)
