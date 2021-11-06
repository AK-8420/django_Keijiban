from django import template

register = template.Library()

@register.filter(name="sample")
def sample(a, b):
    return a + b