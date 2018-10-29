from django import forms
from history.models import foodorders,date,new1

class new(forms.ModelForm):
    class Meta():
        model=date
        fields='__all__'
