from django import template

register = template.Library()

@register.filter
def strip(var):
    return var.strip()

    
