from django import template
from django.shortcuts import render
from ..models import Category

register = template.Library()

@register.filter(name="getCategory_list")
def getCategory_list(request):
    context = {
        'c_list': Category.objects.all(),
    }
    return render(request, '_base.html', context)