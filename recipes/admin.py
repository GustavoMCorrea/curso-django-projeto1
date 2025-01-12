from django.contrib import admin

from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_published', 'created_at', 'updated_at']
    list_filter = ['category', 'is_published']
    search_fields = ['title', 'description']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
