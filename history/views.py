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

        return render(request,'history/history.html',context={'d':dict1,'form':form})

     else:


        print("ERROR");
     return render(request,'history/history.html',context={'form':form})
list1=[];
list2=[];
def showimage(request):
    for n in new1.objects.all():
        list1.append(n.item);
        list2.append(n.frequency);
    plot(list1,list2,linewidth=1.0)
    xlabel('item')
    ylabel('frequency')
    grid(True)
    buffer=io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")
from django.shortcuts import render

# Create your views here.
