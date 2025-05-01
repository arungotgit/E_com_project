from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin
from .models import Category, Sub_Category, Product, Contact_us, Order, Brand

# Register your models here.

admin.site.unregister(User)

@register(User)
class userAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

class CategoryAdmin(ModelAdmin):
    list_display = ['name']

class Sub_CategoryAdmin(ModelAdmin):
    list_display = ['name', 'category'] 

class ProductAdmin(ModelAdmin):
    list_display = ['category', 'sub_category', 'brand', 'name', 'price', 'availability', 'date']

class Contact_usAdmin(ModelAdmin):    
    list_display = ['name', 'email', 'message'] 

class OrderAdmin(ModelAdmin):
    list_display = ['image', 'product', 'quantity', 'total', 'date'] 

class BrandAdmin(ModelAdmin):
    list_display = ['name']
    compressed_fields = ['field1', 'field2']


# class userAdmin(ModelAdmin):
#     list_display = ['username', 'email', 'password1', 'password2']
#     compressed_fields = ['field1', 'field2']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, Sub_CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact_us, Contact_usAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Brand, BrandAdmin)
# admin.site.register(User, userAdmin)


# admin.site.register(Category)
# admin.site.register(Sub_Category)
# admin.site.register(Product)
# admin.site.register(Contact_us)
# admin.site.register(Order)
# admin.site.register(Brand)
