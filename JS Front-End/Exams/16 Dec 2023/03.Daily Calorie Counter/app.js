const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';

//Main variables
const foodInputElement = document.getElementById('food');
const timeInputElement = document.getElementById('time');
const caloriesInputElement = document.getElementById('calories');

const loadMealsButton = document.getElementById('load-meals');
const addMealButton = document.getElementById('add-meal');
const editMealButton = document.getElementById('edit-meal');

let targetId;

const mealsList = document.getElementById('list');

// Event listeners for main buttons
function attachEvents() { // main button events: load, add, edit 
    loadMealsButton.addEventListener('click', loadMeals);
    addMealButton.addEventListener('click', addMeal);
    editMealButton.addEventListener('click', handleEditMeal);
}

// Helper functions
function clearMeals() {
    mealsList.innerHTML = '';
}

function clearAllInputs() {
    foodInputElement.value = '';
    timeInputElement.value = '';
    caloriesInputElement.value = '';
}

function enableAddMealButton() {
    addMealButton.disabled = false;
    editMealButton.disabled = true;
}

function enableEditMealButton() {
    addMealButton.disabled = true;
    editMealButton.disabled = false;
}

function getMealId(mealName) {
    return fetch(BASE_URL)
        .then(response => response.json())
        .then(data => Object.entries(data).find(obj => obj[1].food === mealName)[1]._id); //searches id of a given meal using food name
}

// Functions involving DOM manipulation

async function loadMeals() {
    clearMeals();
    try {
        const response = await fetch(BASE_URL);
        const data = await response.json();
        // console.log(data);
        for (key in data) {
            const mealDiv = document.createElement('div');
            mealDiv.className = 'meal';
            const [food, calories, time] = [data[key].food, data[key].calories, data[key].time];

            const foodEle = document.createElement('h2');
            foodEle.textContent = food;
            mealDiv.appendChild(foodEle);

            const timeEle = document.createElement('h3');
            timeEle.textContent = time;
            mealDiv.appendChild(timeEle);

            const caloriesEle = document.createElement('h3');
            caloriesEle.textContent = calories;
            mealDiv.appendChild(caloriesEle);

            const mealButtonsDiv = document.createElement('div');
            mealButtonsDiv.id = 'meal-buttons';

            const changeButton = document.createElement('button');
            changeButton.className = 'change-meal';
            changeButton.textContent = 'Change';
            changeButton.addEventListener('click', function(event) {
                const targetMeal = event.target.closest('.meal');
                const food = targetMeal.querySelector('h2').textContent;
                const time = targetMeal.querySelector('h3:nth-child(2)').textContent;
                const calories = targetMeal.querySelector('h3:nth-child(3)').textContent;
                enableEditMealButton();
                // console.log(food, time, calories); 
                editMeal(food, time, calories);
            });
            mealButtonsDiv.appendChild(changeButton);

            const deleteButton = document.createElement('button');
            deleteButton.className = 'delete-meal';
            deleteButton.textContent = 'Delete';
            deleteButton.addEventListener('click', function(event) {
                const targetMeal = event.target.closest('.meal');
                const food = targetMeal.querySelector('h2').textContent;
                deleteMeal(food);
            });
            mealButtonsDiv.appendChild(deleteButton);

            mealDiv.appendChild(mealButtonsDiv);
            mealsList.appendChild(mealDiv);
        }
    } catch (error) {
        console.log(error.message);
    }
}

async function editMeal(food, time, calories) {
    targetId = await getMealId(food);// updated current meal Id for meal to be edited, used async because we save info from  fetch in a variable here
    foodInputElement.value = food;
    timeInputElement.value = time;
    caloriesInputElement.value = calories;       
    // enableEditMealButton();
}

function handleEditMeal() { //Meal editing
    // ev.preventDefault();// why necessary?
    const updatedMeal = {
        'calories': caloriesInputElement.value,
        'food': foodInputElement.value,
        'time': timeInputElement.value,
        '_id': targetId,
    }

    fetch(`${BASE_URL}${targetId}`, {
        method: 'PUT',
        headers: { 'Content-type': 'application/json' },
        body: JSON.stringify(updatedMeal),
    })
    .then((response) => {
        if (response.ok) {
            clearAllInputs();
            loadMeals();
            enableAddMealButton();
            targetId = null;
        }
    })
    .catch((error) => console.log(error.message))
}

async function deleteMeal(food) { // Or you can call getMealId(food) and it will return a fetch then continue with .then(id) => and nest the fetch below
    targetId = await getMealId(food);
    // console.log(targetId);

    fetch(`${BASE_URL}${targetId}`, {
        method: 'DELETE'
    })
    .then((response) => {
        if (response.ok) {
            clearMeals(); // First clear already loaded meals
            loadMeals(); // Then load the updated list after meal deletion
            targetId = null;
            enableAddMealButton();//The test doesnt pass when this is not activated here, why no idea; Judge is fine though
        }
    })
    .catch((error) => console.log(error.message))
}

function addMeal() {
    // ev.preventDefault();

    if (foodInputElement.value !== '' && caloriesInputElement.value !== '' && timeInputElement.value !== '') { // dont add empty inputs
        const mealObj = {
            'calories': caloriesInputElement.value,
            'food': foodInputElement.value,
            'time': timeInputElement.value,
        }

        fetch(BASE_URL, {
            method: 'POST',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify(mealObj),
        })
        .then(loadMeals())
        .catch((error) => console.log(error.message))

        clearAllInputs();
    }      
}
    
attachEvents();
        