from django.db import models
from shop .models import product
# Create your models here.
class carts(models.Model):
      cart_id=models.CharField(max_length=250,blank=True)
      date_added=models.DateField(auto_now_add=True)

      class Meta:
            db_table='cart'
            ordering=['date_added']

      def __str__(self):
          return '{}'.format(self.cart_id)

class cart_item(models.Model):
      product2=models.ForeignKey(product,on_delete=models.CASCADE)
      Cart = models.ForeignKey(carts, on_delete=models.CASCADE)
      quantity=models.IntegerField()
      active=models.BooleanField(default=True)
      class Meta:
            db_table='cart_item'
      def subtotal(self):
          return self.product2.price * self.quantity
      def __str__(self):
            return '{}'.format(self.product2)
