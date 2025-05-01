from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Brand sorting

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Product(models.Model):
    availability = (('In Stock', 'In Stock'),('Out Stock', 'Out Stock'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default='')
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=False, default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='ecommerce/pimg', blank=True)
    name = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(blank=True)
    availability = models.CharField(choices=availability,null=True,max_length=100)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email',
    error_messages={'exists': 'Email already registered'})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']
      
    



class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()


    def __str__(self):
        return self.name

# order
class Order(models.Model):
    image = models.ImageField(upload_to='ecommerce/order/image')
    product = models.CharField(max_length=1000, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.CharField(max_length=1000, default='')
    
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
   
    date = models.DateField(default=datetime.datetime.today)


    def __str__(self):
        return self.product
