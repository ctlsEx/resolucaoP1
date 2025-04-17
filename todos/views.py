from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import ListView, CreateView

class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'
    context_object_name = 'todos'



