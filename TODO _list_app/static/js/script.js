document.addEventListener('DOMContentLoaded', () => {
    const todoInput = document.getElementById('todoInput');
    const addTodoBtn = document.getElementById('addTodoBtn');
    const todoList = document.getElementById('todoList');

    // Function to fetch and render all todos
    async function fetchTodos() {
        try {
            const response = await fetch('/todos');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const todos = await response.json();
            renderTodos(todos);
        } catch (error) {
            console.error('Error fetching todos:', error);
            alert('Failed to load tasks. Please try again.');
        }
    }

    // Function to render todos to the UI
    function renderTodos(todos) {
        todoList.innerHTML = ''; // Clear existing list
        if (todos.length === 0) {
            const emptyMessage = document.createElement('li');
            emptyMessage.textContent = "No tasks yet! Add one above.";
            emptyMessage.classList.add('todo-item');
            todoList.appendChild(emptyMessage);
            return;
        }

        todos.forEach(todo => {
            const listItem = document.createElement('li');
            listItem.className = `todo-item ${todo.completed ? 'completed' : ''}`;
            listItem.setAttribute('data-id', todo.id);

            const todoTextSpan = document.createElement('span');
            todoTextSpan.className = 'todo-text';
            todoTextSpan.textContent = todo.text;

            const actionsDiv = document.createElement('div');
            actionsDiv.className = 'todo-actions';

            const toggleCompleteBtn = document.createElement('button');
            toggleCompleteBtn.className = 'toggle-complete-btn';
            toggleCompleteBtn.textContent = todo.completed ? 'Unmark' : 'Complete';
            toggleCompleteBtn.onclick = () => toggleTodoComplete(todo.id, !todo.completed);

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'Delete';
            deleteBtn.onclick = () => deleteTodo(todo.id);

            actionsDiv.appendChild(toggleCompleteBtn);
            actionsDiv.appendChild(deleteBtn);

            listItem.appendChild(todoTextSpan);
            listItem.appendChild(actionsDiv);
            todoList.appendChild(listItem);
        });
    }

    // Add a new todo
    addTodoBtn.addEventListener('click', async () => {
        const todoText = todoInput.value.trim();
        if (!todoText) {
            alert('Task text cannot be empty!');
            return;
        }

        try {
            const response = await fetch('/todos', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: todoText })
            });

            if (response.ok) {
                todoInput.value = ''; // Clear input
                fetchTodos(); // Re-fetch and re-render todos
            } else {
                const errorData = await response.json();
                throw new Error(`Failed to add task: ${errorData.error || response.statusText}`);
            }
        } catch (error) {
            console.error('Error adding todo:', error);
            alert(error.message);
        }
    });

    // Toggle todo completion status
    async function toggleTodoComplete(id, completedStatus) {
        try {
            const response = await fetch(`/todos/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ completed: completedStatus })
            });

            if (response.ok) {
                fetchTodos(); // Re-fetch and re-render todos
            } else {
                const errorData = await response.json();
                throw new Error(`Failed to update task: ${errorData.error || response.statusText}`);
            }
        } catch (error) {
            console.error('Error toggling todo:', error);
            alert(error.message);
        }
    }

    // Delete a todo
    async function deleteTodo(id) {
        if (!confirm('Are you sure you want to delete this task?')) {
            return;
        }
        try {
            const response = await fetch(`/todos/${id}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                fetchTodos(); // Re-fetch and re-render todos
            } else {
                const errorData = await response.json();
                throw new Error(`Failed to delete task: ${errorData.error || response.statusText}`);
            }
        } catch (error) {
            console.error('Error deleting todo:', error);
            alert(error.message);
        }
    }

    // Initial fetch of todos when the page loads
    fetchTodos();
});