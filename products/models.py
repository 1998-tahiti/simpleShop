from django.db import models


class Items(models.Model):
    item_name=models.CharField(max_length=400)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return "/products/%i/" % self.id


class Buyer(models.Model):
    name=models.CharField(max_length=200)
    cartID = models.ForeignKey(Items, on_delete=models.CASCADE)
    qty = models.IntegerField()
    


