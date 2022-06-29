"""Music app url config"""

from django.urls import path

from . import views


app_name = "providers"
urlpatterns = [
    path("", views.show_providers, name="show_providers"),
    path("create-category/", views.create_category, name="create_category"),
    path("create-provider/", views.create_provider, name="create_provider"),
    path("providers/<int:pk>", views.provider_detail, name="provider_detail"),
    path("categorias/", views.show_categories, name="show_categories"),
    path("categorias/<int:pk>", views.category_detail, name="category_detail"),
]
