from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from .models import Review
from products.models import Product
from .forms import ReviewForm

@login_required()
def add_review(request, product_id):
    """
    Add a review for a product.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            review.user_profile = request.user.profile
            review.created_on = timezone.now().date()
            review.save()
            messages.success(request, "Your review has been submitted.")
            return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {'form': form, 'product': product}
    return render(request, template, context)