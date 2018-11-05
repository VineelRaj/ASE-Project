from django.shortcuts import render
from .models import Customer_Food,Order_User


# Create your views here.
def index(request):
    return render(request, 'User/UserAccount.html')
