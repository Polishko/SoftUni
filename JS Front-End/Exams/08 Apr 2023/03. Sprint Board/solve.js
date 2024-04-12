function attachEvents() {
    // Main variables
    const baseURL = 'http://localhost:3030/jsonstore/tasks';

    const taskTitle = document.getElementById('title');
    const taskDescription = document.getElementById('description');

    const taskLists = {
        'ToDo': document.querySelector('#todo-section .task-list'),
        'In Progress': document.querySelector('#in-progress-section .task-list'),
        'Code Review': document.querySelector('#code-review-section .task-list'),
        'Done': document.querySelector('#done-section .task-list'),
    };

    const taskButtonsContent = {
        'ToDo': 'Move to In Progress',
        'In Progress': 'Move to Code Review',
        'Code Review': 'Move to Done',
        'Done': 'Close',
    }

    const taskNextStatus = {
        'ToDo': 'In Progress',
        'In Progress': 'Code Review',
        'Code Review': 'Done',
    }

    const loadBoardBtn = document.getElementById('load-board-btn');
    const addTaskBtn = document.getElementById('create-task-btn');

    loadBoardBtn.addEventListener('click', loadTasks);
    addTaskBtn.addEventListener('click', addTask);


    // Requests
    function loadTasks() {
        // clear data
        clearLists();

        // Create fragment
        const listFragment = document.createDocumentFragment();

        // Load tasks
        fetch(baseURL)
            .then(response => response.json())
            .then(data => {
                Object.values(data).forEach(task => {
                    listFragment.appendChild(createTask(task));
                    taskLists[task.status].appendChild(listFragment);
                });
            });
    }

    function  addTask() {
        const newTask = getInputs();

        if (newTask) {
            fetch(baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newTask),
            })
                .then(response => {
                    if (!response.ok) {
                        return;
                    }
                    clearInputs();
                    return loadTasks();
                })
        }
    }

    function moveTask(task) {
        task.status = taskNextStatus[task.status];
        const taskId = task._id;

        fetch(`${baseURL}/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ taskId, ...task })
        })
            .then(response => {
                if (!response.ok) {
                    return;
                }
                clearLists();
                return loadTasks();
            })
    }

    function deleteTask(task) {
        const taskId = task._id;

        fetch(`${baseURL}/${taskId}`, {
            method: 'DELETE'
        })
            .then(response => {
                if (!response.ok) {
                    return;
                }
                clearLists();
                return loadTasks();
            })
    }

    // Helper functions
    function clearLists() {
        taskLists['ToDo'].innerHTML = '';
        taskLists['In Progress'].innerHTML = '';
        taskLists['Code Review'].innerHTML = '';
        taskLists['Done'].innerHTML = '';
    }

    function clearInputs() {
        taskTitle.value = '';
        taskDescription.value = '';
    }

    function createTask(task) {
        const taskLi = document.createElement('li');
        taskLi.className = 'task';

        const taskTitle = document.createElement('h3');
        taskTitle.textContent = task.title;
        taskLi.appendChild(taskTitle);

        const taskDescription = document.createElement('p');
        taskDescription.textContent = task.description;
        taskLi.appendChild(taskDescription);

        const taskButton = document.createElement('button');
        taskButton.textContent = taskButtonsContent[task.status];
        taskLi.appendChild(taskButton);

        taskButton.addEventListener('click', () => {
            if (task.status !== 'Done') {
                moveTask(task);
            } else {
                deleteTask(task);
            }
        });

        return taskLi;
    }

    function getInputs() {
        if (taskTitle.value !== '' && taskDescription.value !== '') {
            return {
                title: taskTitle.value,
                description: taskDescription.value,
                status: 'ToDo',
            }
        }
    }
}

attachEvents();
