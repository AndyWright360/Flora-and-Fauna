from django.test import TestCase
from .forms import ReviewForm
from .models import Review


class TestReviewForm(TestCase):

    def test_review_title_required(self):
        """
        Tests the title field in the review form is required.
        """
        form = ReviewForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_review_content_required(self):
        """
        Tests the content field in the review form is required.
        """
        form = ReviewForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_review_rating_required(self):
        """
        Tests the rating field in the review form is required.
        """
        form = ReviewForm({'rating': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')
