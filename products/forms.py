from django import forms

class addNewItem(forms.Form):
    item_name=forms.CharField(label="Item Name", max_length=200)
    price=forms.DecimalField(label="Price", max_digits=10, decimal_places=3)
    stock = forms.IntegerField(label="Stock")
