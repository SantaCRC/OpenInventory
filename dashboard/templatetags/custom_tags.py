from django import template
register = template.Library()

@register.simple_tag
def get_location(list, location_id):
    location_id = int(location_id)
    return list[location_id-1]