from django.contrib import admin
from .models import *
admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"
# Register your models here.
admin.site.register(Closes)
admin.site.register(AllUser)
admin.site.register(Category)
admin.site.register(SubCategory)
# admin.site.register(Product)
admin.site.register(shop)
admin.site.register(shopitem)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", 'price',)

