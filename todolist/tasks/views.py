from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from .models import Task
from .utils import get_greeting  # Importa a função de saudação

# View da página inicial (opcional, se não for usada pode ser removida)
def home(request):
    greeting = get_greeting()  # Gera a saudação
    return render(request, 'home.html', {'greeting': greeting})

# View para listar tarefas
def task_list(request):
    user_name = request.GET.get('name', 'Guest')  # Captura o nome do usuário ou usa "Guest" como padrão
    tasks = Task.objects.all()  # Recupera todas as tarefas (pode ser ajustado para filtro por usuário)
    greeting = get_greeting()  # Chama a função de saudação para exibir no template
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'user_name': user_name, 'greeting': greeting})

# View para adicionar uma tarefa
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and title.strip():  # Verifica se o título não está vazio
            Task.objects.create(title=title, description=description)
        else:
            return render(request, 'tasks/task_list.html', {'error': 'O título é obrigatório'})
        return redirect(reverse('task_list') + '?name=' + request.GET.get('name', 'Guest'))

# View para marcar uma tarefa como concluída
def complete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
    except Task.DoesNotExist:
        raise Http404("Tarefa não encontrada")
    return redirect(reverse('task_list') + '?name=' + request.GET.get('name', 'Guest'))
