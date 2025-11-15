from django.shortcuts import render, redirect, get_object_or_404
from .models import Toy, Category, Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    toys = Toy.objects.all()
    return render(request, 'store/home.html', {'toys': toys})

def toy_detail(request, toy_id):
    toy = get_object_or_404(Toy, id=toy_id)
    return render(request, 'store/toy_detail.html', {'toy': toy})

@login_required
def add_to_cart(request, toy_id):
    toy = get_object_or_404(Toy, id=toy_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, toy=toy)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        return redirect('home')

    total = sum(item.total_price for item in cart_items)
    order = Order.objects.create(user=request.user, total_amount=total, is_paid=True)

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            toy=item.toy,
            quantity=item.quantity,
            price=item.toy.price
        )

    cart_items.delete()
    return render(request, 'store/checkout_success.html', {'order': order})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})




def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def toys_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    toys = Toy.objects.filter(category=category)
    return render(request, 'store/toys_by_category.html', {
        'category': category,
        'toys': toys
    })


def toy_list(request):
    toys = Toy.objects.all()
    return render(request, 'store/toy_list.html', {'toys': toys})
