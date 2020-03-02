from django.shortcuts import render, redirect
from .models import Lista
from .forms import Formulario
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = Formulario(request.POST or None)

        if form.is_valid():
            form.save()
            todo_item = Lista.objects.all
            messages.success(request, ("Tarefa adicionada à lista!"))
            return render(request, 'home.html', {'todo_item': todo_item})

    else:
        todo_item = Lista.objects.all
        return render(request, 'home.html', {'todo_item': todo_item})

def about(request):
    return render(request, 'sobre.html', {})

def delete(request, list_id):
    item = Lista.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Tarefa removida da lista!"))
    return redirect('home')

def cross_off(request, list_id):
    item = Lista.objects.get(pk=list_id)
    item.completo = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = Lista.objects.get(pk=list_id)
    item.completo = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = Lista.objects.get(pk=list_id)

        form = Formulario(request.POST or None, instance=item)
        
        if form.is_valid():
            form.save()
            messages.success(request, ("Tarefa editada!"))
            return redirect('home')

    else:
        item = Lista.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})