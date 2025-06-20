from django import template

register = template.Library()

@register.filter(name='multiply_by_200') 
def multiply_by_200(value):
    try:
        return value * 200
    except (ValueError, TypeError):
        return value 