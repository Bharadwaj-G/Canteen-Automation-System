from django.shortcuts import render
from . import form
from .models import Food_items, Quantity

# Create your views here.
def index(request):
    return render(request, 'Manager/index.html')


def Add_food(request):
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
    return render(request, 'Manager/Add_food.html', {'form': f1})
