from django.db import models


class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255, default="")

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Provider(models.Model):
    """Provider model"""
    name = models.CharField(max_length=255)
    direction = models.CharField(max_length=255, default="")
    telefono = models.CharField(max_length=255, default="")
    servicios = models.CharField(max_length=255, default="")
    imagen = models.CharField(max_length=255, default="")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name
