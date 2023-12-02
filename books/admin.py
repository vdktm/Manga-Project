from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Comix


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comix)
class ComixAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
