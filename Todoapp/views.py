from multiprocessing import context
from django.shortcuts import render, redirect

from .models import*
from .forms import *



def home(request):
    lists = List.objects.all()
    context = {'lists': lists}
    return render(request, 'Todoapp/home.html', context)

def create(request):
    form = ListForm()

    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'Todoapp/form.html', context)

def details(request, pk):
    list = List.objects.get(id=pk)
    context = {'list': list}
    return render(request,'Todoapp/details.html', context)


