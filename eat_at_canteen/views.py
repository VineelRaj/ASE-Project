from django.shortcuts import render
# Create your views here.
from Manager.models import Food_items
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect

from django.utils import timezone



from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


import random
def index(request):
    return render(request,'eat_at_canteen/index.html')




def show(request):
    print('added2')
    FoodList = Food_items.objects.order_by('Food_Price')
    print('hii')
    food_dict = {'items': FoodList}
    return render(request, 'eat_at_canteen/order.html', context=food_dict)









