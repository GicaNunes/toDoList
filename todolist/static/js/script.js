console.log("Welcome to the To-Do List!");

document.addEventListener('DOMContentLoaded', () => {
    const taskList = document.getElementById('task-list');

    // Função para salvar tarefas no localStorage
    const saveTasks = () => {
        const tasks = Array.from(taskList.children).map((item) => ({
            text: item.querySelector('.task-text').textContent.trim(),
            completed: item.classList.contains('completed'),
        }));
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    // Função para carregar tarefas do localStorage
    const loadTasks = () => {
        const storedTasks = JSON.parse(localStorage.getItem('tasks')) || [];
        storedTasks.forEach(({ text, completed }) => {
            const taskItem = document.createElement('li');
            taskItem.className = `list-group-item d-flex justify-content-between align-items-center ${completed ? 'completed' : ''}`;
            
            const taskText = document.createElement('span');
            taskText.className = 'task-text';
            taskText.textContent = text;
            taskItem.appendChild(taskText);

            if (!completed) {
                const completeLink = document.createElement('a');
                completeLink.className = 'complete-link btn btn-success btn-sm';
                completeLink.href = '#';
                completeLink.textContent = 'Marcar como concluído';
                taskItem.appendChild(completeLink);
            } else {
                const doneBadge = document.createElement('span');
                doneBadge.className = 'done';
                doneBadge.textContent = '✔ Completed';
                taskItem.appendChild(doneBadge);
            }

            taskList.appendChild(taskItem);
        });
    };

    // Carrega as tarefas ao carregar a página
    loadTasks();

    // Listener para riscar tarefas ou desfazer conclusão
    taskList.addEventListener('click', (e) => {
        if (e.target.classList.contains('complete-link')) {
            e.preventDefault();
            const taskItem = e.target.closest('li');
            taskItem.classList.add('completed');
            e.target.remove(); // Remove o botão "Marcar como concluído"
            const doneBadge = document.createElement('span');
            doneBadge.className = 'done';
            doneBadge.textContent = '✔ Completed';
            taskItem.appendChild(doneBadge);
            saveTasks();
        }
    });

    // Listener para desfazer conclusão (opcional)
    taskList.addEventListener('dblclick', (e) => {
        const taskItem = e.target.closest('li');
        if (taskItem && taskItem.classList.contains('completed')) {
            taskItem.classList.remove('completed');
            const doneBadge = taskItem.querySelector('.done');
            if (doneBadge) doneBadge.remove();

            const completeLink = document.createElement('a');
            completeLink.className = 'complete-link btn btn-success btn-sm';
            completeLink.href = '#';
            completeLink.textContent = 'Marcar como concluído';
            taskItem.appendChild(completeLink);
            saveTasks();
        }
    });

    console.log("To-Do List is loaded and interactive!");
});
