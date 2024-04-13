function attachEvents() {
    // Main variables
    const baseUrl = 'http://localhost:3030/jsonstore/tasks';

    const tasksList = document.getElementById('todo-list');
    const header = document.querySelector('#root h2');
    const titleInput = document.getElementById('title');

    const loadBtn = document.getElementById('load-button');
    loadBtn.addEventListener('click', (e) => {
        e.preventDefault()
        loadTasks()
    });

    const addBtn = document.getElementById('add-button');
    addBtn.addEventListener('click', (e) => {
        e.preventDefault()
        addTask()
    });

    tasksList.addEventListener("click", (e) => {
        if (e.target.textContent === 'Remove') {
            deleteTask(e.target.parentNode.id)
        } else if (e.target.textContent === 'Edit') {
            editTask(e.target.parentNode.id)
        } else if (e.target.textContent === 'Submit') {
            sendUpdate(e.target.parentNode.id)
        }
    })

    // Requests
    function loadTasks() {
        tasksList.innerHTML = '';
        // header.textContent = 'ToDo List';
        const taskFragment = document.createDocumentFragment();

        fetch(baseUrl)
            .then(re => re.json())
            .then(data => {
                Object.values(data).forEach(task => taskFragment.appendChild(createTask(task)));
                tasksList.appendChild(taskFragment);
            })
    }

    function addTask() {
        const newTask = getInput();
        if (newTask) {
            fetch(baseUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newTask)
            })
                .then(re => {
                    if (!re.ok) {
                        return;
                    }
                    clearInput();
                    return loadTasks();
                })
        }
    }

    function deleteTask(id) {

        fetch(`${baseUrl}/${id}`, {
            method: 'DELETE'
        })
            .then(re => {
                if (!re.ok) {
                    return;
                }
                return loadTasks();
            })
    }

    function editTask(id) {
        const targetLi = document.getElementById(`${id}`);

        const newInput = document.createElement('input');
        newInput.value = targetLi.querySelector('span').textContent;
        targetLi.innerHTML = '';
        targetLi.appendChild(newInput);

        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Remove';
        targetLi.appendChild(removeBtn);

        const submitBtn = document.createElement('button');
        submitBtn.textContent = 'Submit';
        targetLi.appendChild(submitBtn);
    }

    function sendUpdate(id) {
        const newTitle = document.getElementById(`${id}`).querySelector('input').value;

        fetch(`${baseUrl}/${id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: newTitle })
        })
            .then(re => {
                if (!re.ok) {
                    return;
                }
                return loadTasks();
            })
    }

    // Helper functions
    function createTask(task) {
        const liItem = document.createElement('li');
        liItem.id = task._id;
        const spanItem = document.createElement('span');
        spanItem.textContent = task.name;
        liItem.appendChild(spanItem);

        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Remove';
        liItem.appendChild(removeBtn);

        const editBtn = document.createElement('button');
        editBtn.textContent = 'Edit';
        liItem.appendChild(editBtn);

        removeBtn.addEventListener('click', () => deleteTask(task));
        editBtn.addEventListener('click', (e) => editTask(task, e));

        return liItem;
    }

    function getInput() {
        if (titleInput.value !== '') {
            return {
                name: titleInput.value,
            };
        }
    }

    function clearInput() {
        titleInput.value = '';
    }
}

attachEvents();
