from django import template
from ..models import Category

register = template.Library()

@register.filter(name="getCategory_list")
def getCategory_list():
    return Category.object.all()