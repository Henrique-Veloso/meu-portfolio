from django import template

register = template.Library()

@register.filter(name='split_string')
def split_string(value, arg):
    if isinstance(value, str):
        return [item.strip() for item in value.split(arg)]
    return value
