from django import forms


class Add_food(forms.Form):
    Id = forms.IntegerField()
    Name = forms.CharField()
    Price = forms.FloatField()
    Quantity = forms.IntegerField()


class get_id(forms.Form):
    Id = forms.IntegerField()


class Add_tables(forms.Form):
    Id = forms.IntegerField()
    availability = forms.BooleanField(required=False)
