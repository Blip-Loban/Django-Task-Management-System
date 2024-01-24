from django.shortcuts import render,redirect
from .forms import *
# Create your views here.
def add_category(request):
     
    if request.method=='POST':
        category_form= CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('homepage')
    else :
        category_forms=CategoryForm()

    return render(request,'add_category.html',{'forms':category_forms})