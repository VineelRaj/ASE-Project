from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from history.models import foodorders,date,new1
from history.forms import new
from matplotlib import pylab
from pylab import *
import PIL,PIL.Image
import io
from io import BytesIO



def history(request):
    return render(request,'history/history.html',{'title':'history'})

def users(request):

     form=new()
     if request.method == "POST":
         form=new(request.POST)

     if form.is_valid():

        form.save(commit=True)
        form=new()

        dict1={}
        all_date=date.objects.all();
        all_foodorders=foodorders.objects.all();

        for d in all_date:
            d1=d.FROM;
            d2=d.TO;
            print(d1)
            print(d2)
            for fo in all_foodorders:
                if fo.date>=d1 and fo.date<=d2:
                   dict1[fo.foodname]=0;
            for fo in all_foodorders:
                if fo.date>=d1 and fo.date<=d2:
                   dict1[fo.foodname]=dict1[fo.foodname]+fo.quantity;

        print(dict1)
        emp=new1.objects.all()
        emp.delete()
        emp1=date.objects.all()
        emp1.delete()
        for key,value in dict1.items():
            print(key,value)
            p=new1(item=key,frequency=value)
            p.save()
            dict2={}

        return render(request,'history/history.html',context={'d':dict1,'d1':dict2,'form':form})

     else:


        print("ERROR");
     return render(request,'history/history.html',context={'form':form})
