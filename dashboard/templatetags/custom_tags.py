from django import template
from django.conf import settings


register = template.Library()


# Helper function to get location
@register.simple_tag
def get_location(list, location_id):
    location_id = int(location_id)
    return list[location_id-1]

# Helper function to get category
@register.simple_tag
def get_category(list, category_id):
    category_id = int(category_id)
    return list[category_id-1]

# Helper function to get settings from settings.py
@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")

# Helper function to get storage
@register.simple_tag
def get_storage(list, storage_id):
    storage_id = int(storage_id)
    return list[storage_id-1]