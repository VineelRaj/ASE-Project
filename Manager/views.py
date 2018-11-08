from django.shortcuts import render
from . import form
from .models import Food_items, Quantity, Tables, Available_Towns


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
    f2 = form.get_id()
    if request.method == 'POST':
        f2 = form.get_id(request.POST)
        if f2.is_valid():
            fid = f2.cleaned_data['Id']
            f_item = Food_items.objects.get(Food_id__exact=fid)
            Quantity.objects.get(Food_id__exact=fid).delete()
            f_item.delete()
            return render(request, 'Manager/index.html')
    item = Food_items.objects.all()
    content = {'form': f2, 'item': item}
    return render(request, 'Manager/Remove_food.html', content)


def update_food(request):
    if request.method == "POST":
        f_id = request.POST['f_Id']
        update = Food_items.objects.get(Food_id=f_id)
        qu_update = Quantity.objects.get(Food_id__exact=f_id)
        content = {'update': update, 'qu_update': qu_update}
        return render(request, 'Manager/Update_food.html', content)
    else:
        item = Food_items.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Update_food.html', content)


def check_update_food(request):
    if request.method == "POST":
        f_id = request.POST['Id']
        name = request.POST['Name']
        price = request.POST['Price']
        food_temp = Food_items.objects.get(Food_id=f_id)
        food_temp.Food_Name = name
        food_temp.Food_Price = price
        food_temp.save()
        qu = request.POST['quantity']
        if qu > 0:
            qu_temp = Quantity.objects.get(Food_id=f_id)
            qu_temp.quantity = qu
            qu_temp.save()
    item = Food_items.objects.all()
    content = {'item': item}
    return render(request, 'Manager/Update_food.html', content)


def food_home(request):
    return render(request, 'Manager/Food_home.html')


def tables_home(request):
    return render(request, 'Manager/tables_home.html')


def remove_tables(request):
    f2 = form.get_id()
    if request.method == 'POST':
        f2 = form.get_id(request.POST)
        if f2.is_valid():
            fid = f2.cleaned_data['Id']
            Tables.objects.get(Table_id__exact=fid).delete()
            return render(request, 'Manager/tables_home.html')
    item = Tables.objects.all()
    content = {'form': f2, 'item': item}
    return render(request, 'Manager/Remove_table.html', content)


def add_tables(request):
    f1 = form.Add_tables()
    if request.method == 'POST':
        f1 = form.Add_tables(request.POST)
        if f1.is_valid():
            fid = f1.cleaned_data['Id']
            availabilty = f1.cleaned_data['availability']
            Tables.objects.create(Table_id=fid, availability=availabilty)
            return render(request, 'Manager/tables_home.html')
    return render(request, 'Manager/Add_tables.html', {'form': f1})


def town_home(request):
    return render(request, 'Manager/town_home.html')


def remove_towns(request):
    f2 = form.Add_city()
    if request.method == 'POST':
        f2 = form.Add_city(request.POST)
        if f2.is_valid():
            fname = f2.cleaned_data['town']
            Available_Towns.objects.get(Towns__exact=fname).delete()
            return render(request, 'Manager/town_home.html')
    item = Available_Towns.objects.all()
    content = {'form': f2, 'item': item}
    return render(request, 'Manager/Remove_town.html', content)


def add_towns(request):
    f1 = form.Add_city()
    if request.method == 'POST':
        f1 = form.Add_city(request.POST)
        if f1.is_valid():
            fname = f1.cleaned_data['town']
            Available_Towns.objects.create(Towns=fname)
            return render(request, 'Manager/town_home.html')
    return render(request, 'Manager/Add_town.html', {'form': f1})


def check_update_table(request):
    if request.method == "POST":
        f_id = request.POST['Id']
        ava = request.POST['availability']
        table_temp = Tables.objects.get(Table_id=f_id)
        table_temp.availability = ava
        table_temp.save()
        item = Tables.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Update_tables.html', content)
    else:
        item = Tables.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Update_tables.html', content)


def update_table(request):
    if request.method == "POST":
        f_id = request.POST['f_Id']
        update = Tables.objects.get(Table_id=f_id)
        content = {'update': update}
        return render(request, 'Manager/Update_tables.html', content)
    else:
        item = Tables.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Update_tables.html', content)
