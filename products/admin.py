from django.contrib import admin
from .models import Clothing, Category, Accessories

# Register your models here.
admin.site.register(Clothing)
admin.site.register(Category)
admin.site.register(Accessories)