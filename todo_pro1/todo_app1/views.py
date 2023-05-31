from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import todo_task
from . forms import todo_form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.


class task_delete_view(DeleteView):
    model=todo_task
    template_name='delete.html'
    success_url=reverse_lazy('todo_app1:cbv')


class task_update_view(UpdateView):
    model=todo_task
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todo_app1:cbv_detail',kwargs={'pk':self.object.id})


class task_list_view(ListView):
    model=todo_task
    template_name='index.html'
    context_object_name='task1'


class task_detail_view(DetailView):
    model=todo_task
    template_name='detail.html'
    context_object_name='task'





def add(request):
    task1=todo_task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=todo_task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"index.html",{'task1':task1})


#def delete(request,task_id):
 #    task=todo_task.objects.get(id=task_id)
 #    if request.method=="POST":
  #       task.delete()
   #      return redirect('/')
 #    return render(request,"delete.html")


def delete(request,task_id):
    task=todo_task.objects.get(id=task_id)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,"delete.html")


def update(request,task_id):
    task=todo_task.objects.get(id=task_id)
    f=todo_form(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'task':task})
