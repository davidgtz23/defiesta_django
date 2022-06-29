
from django.shortcuts import render

from providers.models import Provider, Category


def home(request):
    providers = Provider.objects.all()
    categories = Category.objects.all()
    return render(request, "home.html", {"providers": providers, "categories": categories})
