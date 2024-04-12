window.addEventListener('load', solve);

function solve() {
    let taskCounter = 0;
    let totalSprintPoints = 0;

    const labels = {
        'Feature': ['&#8865', 'feature'],
        'Low Priority Bug': ['&#9737', 'low-priority'],
        'High Priority Bug': ['&#9888', 'high-priority'],
    }

    // Main elements
    const titleInput = document.getElementById('title');
    const descriptionInput = document.getElementById('description');
    const labelInput = document.getElementById('label');
    const estimationInput = document.getElementById('points');
    const assigneeInput = document.getElementById('assignee');

    const createTaskButton = document.getElementById('create-task-btn');
    const deleteTaskButton = document.getElementById('delete-task-btn');

    const tasksSection = document.getElementById('tasks-section');

    const taskInfoElement = document.getElementById('task-id');

    createTaskButton.addEventListener('click', function() {
        const currentTask = getInputs();
        if (currentTask) {
            taskInfoElement.value = `task-${taskCounter += 1}`;
            createTask(currentTask);
            applyTotalSprintPoints();
            clearInputs();
        }
    });

    deleteTaskButton.addEventListener('click', function(e) {
        const taskId = document.getElementById('task-id').value;
        const taskTarget = document.getElementById(taskId);
        taskTarget.remove();
        applyTotalSprintPoints();
        clearInputs();
        enableInputs();
        enableCreateTask();
    });

    // check inputs
    function getInputs() {
        if (titleInput.value !== '' && descriptionInput.value !== ''
            && labelInput.value !== '' && estimationInput.value !== '' && assigneeInput.value !== '') {
            return {
                title: titleInput.value,
                description: descriptionInput.value,
                label: labelInput.value,
                estimationPoints: Number(estimationInput.value),
                assignee: assigneeInput.value,
            }
        }
    }

    function createTask(task) {
        const taskArticle = document.createElement('article');
        taskArticle.id = document.getElementById('task-id').value;
        taskArticle.className = 'task-card';
        tasksSection.appendChild(taskArticle);

        const featureDiv = document.createElement('div');
        featureDiv.className = `task-card-label ${labels[task.label][1]}`;
        featureDiv.innerHTML = `${task.label} ${labels[task.label][0]}`;
        taskArticle.appendChild(featureDiv);

        const taskTitle = document.createElement('h3');
        taskTitle.className = 'task-card-title';
        taskTitle.textContent = task.title;
        taskArticle.appendChild(taskTitle);

        const taskDescription = document.createElement('p');
        taskDescription.className = 'task-card-description';
        taskDescription.textContent = task.description;
        taskArticle.appendChild(taskDescription);

        const taskPoints = document.createElement('div');
        taskPoints.className = 'task-card-points';
        taskPoints.textContent = `Estimated at ${task.estimationPoints} pts`;
        taskArticle.appendChild(taskPoints);

        const taskAssignee = document.createElement('div');
        taskAssignee.className = 'task-card-assignee';
        taskAssignee.textContent = `Assigned to: ${task.assignee}`;
        taskArticle.appendChild(taskAssignee);

        const taskActions = document.createElement('div');
        taskActions.className = 'task-card-actions';
        taskArticle.appendChild(taskActions);

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        taskActions.appendChild(deleteButton);

        totalSprintPoints += task.estimationPoints;

        deleteButton.addEventListener('click', () => prepareForDeletion(task, taskArticle.id));
    }

    function prepareForDeletion(task, id) {
        updateInputs(task, id);
        enableDeleteTask();
        disableInputs();
        totalSprintPoints -= task.estimationPoints;
    }

    function enableDeleteTask() {
        createTaskButton.setAttribute('disabled', 'disabled');
        deleteTaskButton.removeAttribute('disabled');
    }

    function enableCreateTask() {
        deleteTaskButton.setAttribute('disabled', 'disabled');
        createTaskButton.removeAttribute('disabled');
    }

    function updateInputs(task, id) {
        titleInput.value = task.title;
        descriptionInput.value = task.description;
        labelInput.value = task.label;
        estimationInput.value = task.estimationPoints;
        assigneeInput.value = task.assignee;
        taskInfoElement.value = id;
    }

    function disableInputs() {
        titleInput.setAttribute('disabled', 'disabled');
        descriptionInput.setAttribute('disabled', 'disabled');
        labelInput.setAttribute('disabled', 'disabled');
        estimationInput.setAttribute('disabled', 'disabled');
        assigneeInput.setAttribute('disabled', 'disabled');
    }

    function enableInputs() {
        titleInput.removeAttribute('disabled');
        descriptionInput.removeAttribute('disabled');
        labelInput.removeAttribute('disabled');
        estimationInput.removeAttribute('disabled');
        assigneeInput.removeAttribute('disabled');
    }

    function applyTotalSprintPoints(task) {
        const pointsPa = document.getElementById('total-sprint-points');
        pointsPa.textContent = `Total Points ${totalSprintPoints}pts`;
    }

    function clearInputs() {
        titleInput.value = '';
        descriptionInput.value = '';
        labelInput.value = '';
        estimationInput.value = '';
        assigneeInput.value = '';
        taskInfoElement.value = '';
    }
}