from django import template

register = template.Library()

@register.filter(name='multiply_by_200')
def multiply_by_200(value):
    try:
        return value * 200
    except (ValueError, TypeError):
        return value

@register.filter(name='split_string') 
def split_string(value, delimiter):
    
    if not isinstance(value, str):
        return value 
    return value.split(delimiter)