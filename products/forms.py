from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Range


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        range = Range.objects.all()
        friendly_names = [(r.id, r.get_friendly_name()) for r in range]

        self.fields['range'].choices = friendly_names
