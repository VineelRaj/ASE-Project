from django import forms


class Add_food(forms.Form):
    Id = forms.IntegerField()
    Name = forms.CharField()
    Price = forms.FloatField()
    Quantity = forms.IntegerField()


class Remove_food(forms.Form):
    Id = forms.IntegerField()
