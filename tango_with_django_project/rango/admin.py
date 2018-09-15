#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin

from rango.models import Category, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'category', 'views']
    list_filter = ['title']
    search_fields = ['title']
    fieldsets = [
        ('Página', {'fields': ['category', 'title', 'url']}),
        ('Views', {'fields': ['views']})
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes']
    list_filter = ['name']
    search_fields = ['name', 'likes']
    fieldsets = [
        ('Categoria', {'fields': ['name']}),
        ('Curtidas e visualizações', {'fields': ['views', 'likes']})
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
