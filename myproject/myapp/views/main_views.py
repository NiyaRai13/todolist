from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Task
from django.contrib.auth.decorators import login_required

def index(request):
    data = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': data})

@login_required
def createlist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Task.objects.create(
                title=title, 
                description=description
            )
            return redirect('index')
    return render(request, 'main/create_list.html')

def editlist(request, id):
    task = Task.objects.get( id=id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('index')
    return render(request, 'main/edit.html', {'task': task})

def deletelist(request, id):
    task=Task.objects.filter(id=id)
    task.delete()

    return redirect("index")