from django.contrib import admin

# Register your models here.
from .models import Category, CategoryAdmin, MenuItem
admin.site.register(MenuItem)
admin.site.register(Category, CategoryAdmin)