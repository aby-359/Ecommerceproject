from .models import carts,cart_item
from .views import cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            Cart=carts.objects.filter(cart_id=cart_id(request))
            cart_items=cart_item.objects.filter(Cart=Cart[:1])
            for Cart_Items in cart_items:
                item_count += Cart_Items.quantity
        except carts.DoesNotExist:
            item_count=0
        return dict(item_count=item_count)
