from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class SubcategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = ProductAdminForm

class PageAdminForm(forms.ModelForm):
    context = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Page
        fields = '__all__'

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PageAdminForm



class AdminOrderBasket(admin.TabularInline):
    model = OrderBasket
    fields = ('product','size','color','quantity',)

class AdminOrder(admin.ModelAdmin):
    model = Order
    inlines = (AdminOrderBasket,)

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Subcategories, SubcategoriesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(ActionCatogory)
admin.site.register(Basket)
admin.site.register(Comments)
admin.site.register(Photos)

admin.site.register(Order, AdminOrder)



