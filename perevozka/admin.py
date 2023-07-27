from django.contrib import admin
from .models import *


class OrdersAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "telephone", "organization",
    "full_text", "status", "time" )

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "full_text", "time" )

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "time", "full_text", "image", "published" )
    prepopulated_fields = {"slug": ("title",)}

class TrucksAdmin(admin.ModelAdmin):
    list_display = ("tipe", "image", "tonnage", "model", "price" )

admin.site.register(Orders, OrdersAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Trucks, TrucksAdmin)
