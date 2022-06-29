from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Provider, Category


def show_providers(request):
    providers = Provider.objects.all()
    return render(request, "providers/show-providers.html", {"providers": providers})


@login_required
def provider_detail(request, pk):
    provider = Provider.objects.get(pk=pk)
    return render(request, "providers/provider-detail.html", {"provider": provider})


@login_required
def create_category(request):
    if request.method == "POST":
        name = request.POST["name"]
        category = Category(name=name)
        category.save()
        return redirect("providers:show_providers")
    else:
        return render(request, "providers/create-category.html",)


@login_required
def create_provider(request):
    if request.method == "POST":
        name = request.POST["name"]
        category_id = request.POST["category_id"]
        direction = request.POST["direction"]
        telefono = request.POST["telefono"]
        servicios = request.POST["servicios"]
        imagen = request.POST["imagen"]
        provider = Provider(name=name, category_id=category_id, direction=direction, telefono=telefono, servicios=servicios, imagen=imagen)
        provider.save()
        return redirect("providers:show_providers")
    else:
        categories = Category.objects.all()
        return render(request, "providers/create-provider.html", {"categories": categories})



# CATEGORIAS
def show_categories(request):
    categories = Category.objects.all()
    return render(request, "providers/show-categories.html", {"categories": categories})

@login_required
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    providers = Provider.objects.filter(category_id=pk)
    return render(request, "providers/category-detail.html", {"category": category, "providers": providers})

