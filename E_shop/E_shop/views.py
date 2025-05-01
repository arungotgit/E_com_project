from django.shortcuts import render, redirect,HttpResponse
from app.models import Category, Sub_Category, Product, Brand, Contact_us, Order
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from app.models import UserCreateForm
from django.contrib.auth.models import User
from django.views.generic import ListView

def Master(request):
    return render(request, 'master.html')



def Index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')

    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')

    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product': product,
        'brand': brand,
    }
    return render(request, 'index.html', context)


# signup view here
def signup(request):
    if request.method== 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']

            )
            login(request, new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

    context = {
        'form':form,
    }
    return render(request, 'registration/signup.html',context)




# cart veiws here....

@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')



# contact page view here
def contact(request):
    if request.method == 'POST':
        contact = Contact_us(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        contact.save()
    return render(request, 'contact-us.html')

# checkout page view here
def Checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)

        print(cart)
        
        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b
          
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                pincode = pincode,
                total = total,
                phone = phone,
            )
            order.save()
        request.session['cart'] = {}
        return redirect("index")
    return HttpResponse('This is checkout page')



# your oder view here
def Your_Order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)

    order = Order.objects.filter(user=user)
    print(user, order)
    context = {
        'order': order,
    }
    return render(request, 'yourOrder.html', context)


# product page view here

def Product_detail(request):
    category = Category.objects.all()

    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')



    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')

    else:
        product = Product.objects.all()

    context = {
         'category': category,
         'brand': brand,
         'product': product,

    }
    return render(request, 'product_detail.html', context)


# product_detail page

def Product_page(request,id):
    product = Product.objects.filter(id = id).first()
    context = {
        'product': product,
    }
    return render(request, 'product_page.html', context)


# Search page view here
def Search(request):
    search_input = request.GET['search']
    product = Product.objects.filter(name__icontains = search_input)
    context = {
        'product' : product,
    }
    return render(request, 'search.html', context)
