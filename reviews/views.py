from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from .models import Review
from products.models import Product
from django.contrib.auth.models import User
from .forms import ReviewForm

@login_required()
def add_review(request, product_id):
    """
    Add a review for a product.
    """
    product = get_object_or_404(Product, pk=product_id)
    user = User.objects.get(username=request.user)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            review.user = user
            review.created_on = timezone.now().date()
            review.save()

            # Calculate the average rating for the product
            product.average_rating()

            messages.success(request, "Your review has been submitted.")
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ReviewForm()
        
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product
        }
    return render(request, template, context)

@login_required()
def edit_review(request, review_id):
    """
    Edit a review for a product.
    """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    referer_url = request.META.get('HTTP_REFERER')

    if request.user != review.user:
        messages.error(request, "You don't have authorisation to edit this review.")
        if referer_url and '/reviews/' not in referer_url:
            return redirect(referer_url)
        else:
            return redirect(reverse('product_detail', args=[product.id]))

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()

            # Update the average rating for the product
            product.average_rating()

            messages.success(request, "Your review has been updated.")
            if referer_url and '/reviews/' not in referer_url:
                return redirect(referer_url)
            else:
                return redirect(reverse('product_detail', args=[product.id]))
    
    else:
        form = ReviewForm(instance=review)
    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product': product
        }
    return render(request, template, context)

@login_required()
def delete_review(request, review_id):
    """
    Delete a review for a product.
    """
    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    referer_url = request.META.get('HTTP_REFERER')

    if not request.user.is_superuser:
        if request.user != review.user:
            messages.error(request, "You don't have authorisation to edit this review.")
            if referer_url and '/reviews/' not in referer_url:
                return redirect(referer_url)
            else:
                return redirect(reverse('product_detail', args=[product.id]))

    review.delete()

    # Update the average rating for the product
    product.average_rating()

    messages.success(request, "Your review has been deleted.")
    if referer_url and '/reviews/' not in referer_url:
        return redirect(referer_url)
    else:
        return redirect(reverse('product_detail', args=[product.id]))
