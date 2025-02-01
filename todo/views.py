from django.urls import reverse_lazy
from .forms import RegistForm, UpdateForm
from .models import Task
from django.shortcuts import render
from django.views.generic import DetailView,CreateView,TemplateView,ListView,DeleteView,UpdateView

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistView(CreateView): #taskを追加するページ
    model = Task
    template_name = 'todo/regist_task.html'
    form_class = RegistForm
    success_url = reverse_lazy('todo:home')

class TaskListView(ListView): #task一覧を表示するページ
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        query = super().get_queryset()
        task_title = self.request.GET.get('task_title', None) 
        task_expiry = self.request.GET.get('task_expiry', None)

        if task_title:
            query = query.filter(title__icontains=task_title)

        if task_expiry:
            query = query.filter(expiry=task_expiry)

        return query

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class TaskDeleteView(DeleteView): #taskを削除するページ
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('todo:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = UpdateForm
    template_name = 'todo/task_update.html'
    success_url = reverse_lazy('todo:task_list')