from django.db import models
from django.contrib.auth.models import User  # Caso você queira vincular tarefas a usuários

class Task(models.Model):
    # Campos básicos da tarefa
    title = models.CharField(max_length=200)  # Título da tarefa
    description = models.TextField(blank=True, null=True)  # Descrição (opcional)
    completed = models.BooleanField(default=False)  # Status de conclusão
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

    # Exemplo de campo opcional para prioridade
    priority = models.CharField(
        max_length=10,
        choices=[
            ('Low', 'Baixa'),
            ('Medium', 'Média'),
            ('High', 'Alta')
        ],
        default='Medium'
    )

    # Se quiser associar uma tarefa a um usuário
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # Exclui as tarefas se o usuário for deletado
        related_name='tasks',  # Permite acesso às tarefas do usuário (user.tasks.all())
        blank=True,  # Torna o campo opcional
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', '-created_at']  # Ordenação: concluídas por último, mais novas primeiro
