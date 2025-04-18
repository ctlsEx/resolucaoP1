from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import ListView, CreateView

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    template_name = 'todos/todo_form.html'
    success_url = reverse_lazy('todo_list')
