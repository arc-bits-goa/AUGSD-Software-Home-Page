from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

# Create your views here.

def index(request):
    projects = Portal.objects.all()
    scripts = Script.objects.all()
    
    context = {'projects':projects, 'scripts':scripts}
    return render(request, 'list.html', context)

# def addProject(request):
#     projects = Portal.objects.all()
    
#     form = PortalForm()

#     if request.method =='POST':
#         form = PortalForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')


#     context = {'projects':projects, 'form':form}
#     return render(request, 'add.html', context)

# def baseProject(request):
    
#     return render(request, 'base.html', {})
    

# def updateProject(request, pk):
# 	project = Portal.objects.get(id=pk)

# 	form = PortalForm(instance=project)

# 	if request.method == 'POST':
# 		form = PortalForm(request.POST, instance=project)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}

# 	return render(request, 'update.html', context)

# def deleteProject(request, pk):
# 	item = Portal.objects.get(id=pk)

# 	if request.method == 'POST':
# 		item.delete()
# 		return redirect('/')

# 	context = {'item':item}
# 	return render(request, 'delete.html', context)
