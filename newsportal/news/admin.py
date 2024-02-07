from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_filter = ['postCategory', 'author']
    search_fields = ('title', 'postCategory__title')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
