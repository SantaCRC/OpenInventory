from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        
    name = forms.CharField(label='Name', max_length=200, widget=forms.TextInput(attrs={
      'class': 'input',
       'placeholder' : 'Enter Name Here '
     }))
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category','image']