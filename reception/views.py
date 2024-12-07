from django.shortcuts import render, get_object_or_404, redirect
from .models import Visitor
from .forms import VisitorForm

def home(request):
    return render(request, 'home.html')

def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors_list.html', {'visitors': visitors})

def register_visitor(request):
    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm()
    return render(request, 'register.html', {'form': form})

def update_visitor(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == "POST":
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitor_list')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'register.html', {'form': form})

def delete_visitor(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == "POST":
        visitor.delete()
        return redirect('visitor_list')
    return render(request, 'delete_visitor.html', {'visitor': visitor})
