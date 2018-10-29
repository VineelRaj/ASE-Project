from django.shortcuts import render
from . import form
from .models import Food_items, Quantity


# Create your views here.
def index(request):
    return render(request, 'Manager/index.html')


def add_food(request):
    f1 = form.Add_food()
    if request.method == 'POST':
        f1 = form.Add_food(request.POST)
        if f1.is_valid():
            fid = f1.cleaned_data['Id']
            name = f1.cleaned_data['Name']
            price = f1.cleaned_data['Price']
            qu = f1.cleaned_data['Quantity']
            f_item = Food_items.objects.create(Food_id=fid, Food_Name=name, Food_Price=price)
            Quantity.objects.create(Food_id=f_item, quantity=qu)
            return render(request, 'Manager/index.html')
    return render(request, 'Manager/Add_food.html', {'form': f1})


def remove_food(request):
    f2 = form.Remove_food()
    if request.method == 'POST':
        f2 = form.Remove_food(request.POST)
        if f2.is_valid():
            fid = f2.cleaned_data['Id']
            f_item = Food_items.objects.get(Food_id__exact=fid)
            Quantity.objects.get(Food_id__exact=fid).delete()
            f_item.delete()
            return render(request, 'Manager/index.html')
    item = Food_items.objects.all()
    content = {'form': f2, 'item': item}
    return render(request, 'Manager/Remove_food.html', content)
