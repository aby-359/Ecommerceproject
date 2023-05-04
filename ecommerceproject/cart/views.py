from django.shortcuts import render, redirect, get_object_or_404
from shop .models import product
from .models import carts,cart_item
from django.core.exceptions import ObjectDoesNotExist
def cart_id(request):
    Cart = request.session.session_key
    if not Cart:
        Cart = request.session.create()
    return Cart

def add_cart(request,product_id):
    product2 = product.objects.get(id=product_id)
    try:
        Cart = carts.objects.get(cart_id=cart_id(request))
    except carts.DoesNotExist:
        Cart = carts.objects.create(cart_id=cart_id(request))
        Cart.save()
    try:
        Cart_item=cart_item.objects.get(product2=product2,Cart=Cart)
        if Cart_item.quantity < Cart_item.product2.stock:
           Cart_item.quantity += 1
           Cart_item.save()
    except cart_item.DoesNotExist:
        Cart_item = cart_item.objects.create(
            product2=product2,
            quantity=1,
            Cart=Cart)
        Cart_item.save()

    return redirect('cart:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
       Cart=carts.objects.get(cart_id=cart_id(request))
       cart_items=cart_item.objects.filter(Cart=Cart,active=True)
       for  Cart_item in cart_items:
            total+=( Cart_item.product2.price *  Cart_item.quantity)
            counter+= Cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    Cart=carts.objects.get(cart_id=cart_id(request))
    product2=get_object_or_404(product,id=product_id)
    Cart_item=cart_item.objects.get(product2=product2,Cart=Cart)
    if Cart_item.quantity > 1:
        Cart_item.quantity -= 1
        Cart_item.save()
    else:
        Cart_item.delete()
    return redirect('cart:cart_detail')

def full_remove(request,product_id):
    Cart = carts.objects.get(cart_id=cart_id(request))
    product2 = get_object_or_404(product, id=product_id)
    Cart_item = cart_item.objects.get(product2=product2, Cart=Cart)
    Cart_item.delete()
    return redirect('cart:cart_detail')