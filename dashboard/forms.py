from django import forms
from .models import Product, Category, Storage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False # hide labels
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category','image']

class CategoryForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(CategoryForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False # hide labels
  class Meta:
      model = Category
      fields = ['name', 'description', 'parent_category']
      
class StorageForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(StorageForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False # hide labels
  class Meta:
      model = Storage
      fields = ['name', 'description', 'location', 'parent_storage']