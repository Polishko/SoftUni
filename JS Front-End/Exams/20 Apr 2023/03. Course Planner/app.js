// Main variables
const baseUrl = 'http://localhost:3030/jsonstore/tasks';
const courseNameInput = document.getElementById('course-name');
const courseTypeInput = document.getElementById('course-type');
const courseDescriptionInput = document.getElementById('description');
const teacherNameInput = document.getElementById('teacher-name');

const loadCourseButton = document.getElementById('load-course');
const addCourseButton = document.getElementById('add-course');
const editCourseButton = document.getElementById('edit-course');

const courseList = document.getElementById('list');
const formContainer = document.getElementById('form');

loadCourseButton.addEventListener('click', loadCourses);
addCourseButton.addEventListener('click', addCourse);
editCourseButton.addEventListener('click', sendChange);

// Helper functions
function createCourse(course) {
    const courseDiv = document.createElement('div');
    courseDiv.className = 'container';
    courseDiv.setAttribute('data-id', course._id);

    const courseName = document.createElement('h2');
    courseName.textContent = course.title;
    courseDiv.appendChild(courseName);

    const courseTeacher = document.createElement('h3');
    courseTeacher.textContent = course.teacher;
    courseDiv.appendChild(courseTeacher);

    const courseType = document.createElement('h3');
    courseType.textContent = course.type;
    courseDiv.appendChild(courseType);

    const courseDescription = document.createElement('h4');
    courseDescription.textContent = course.description;
    courseDiv.appendChild(courseDescription);

    const editButton = document.createElement('button');
    editButton.className = 'edit-btn';
    editButton.textContent = 'Edit Course';
    courseDiv.appendChild(editButton);

    const finishButton = document.createElement('button');
    finishButton.className = 'finish-btn';
    finishButton.textContent = 'Finish Course';
    courseDiv.appendChild(finishButton);

    editButton.addEventListener('click', (e) => editCourse(e, course));
    finishButton.addEventListener('click', (e) => finishCourse(e));

    return courseDiv;
}

function clearAllInputs() {
    courseNameInput.value = '';
    courseTypeInput.value = '';
    courseDescriptionInput.value = '';
    teacherNameInput.value = '';
}

function getInputData() {
    if (courseNameInput.value !== '' && courseTypeInput.value !== '' && courseDescriptionInput.value !== '' && teacherNameInput.value !== '') {
        return {
            title: courseNameInput.value,
            type: courseTypeInput.value,
            description: courseDescriptionInput.value,
            teacher: teacherNameInput.value,
        }
    }
}

function activateEditButton() {
    editCourseButton.removeAttribute('disabled');
    addCourseButton.setAttribute('disabled', 'disabled');
}

function activateAddButton() {
    editCourseButton.setAttribute('disabled', 'disabled');
    addCourseButton.removeAttribute('disabled');
}

// Requests
function loadCourses() {
    // Clear list
    courseList.innerHTML = '';

    // Create fragment
    const courseListFragment = document.createDocumentFragment();

    // Load courses
    fetch(baseUrl)
        .then((response) => response.json())
        .then((data) => {
            Object.values(data).forEach(course => courseListFragment.appendChild(createCourse(course)));
            courseList.appendChild(courseListFragment);
        })

    // Deactivate editCourseBtn and activate AddCourseBtn
    activateAddButton();
}

function addCourse() {
    // get input data
    const newCourse = getInputData();

    // post course
    if (newCourse) {
        fetch(baseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newCourse)

        })
            .then(response => {
                if (!response.ok) {
                    return ;
                }
                // clear inputs
                clearAllInputs();
                // load courses
                return loadCourses();
            })
    }
}

function editCourse(e, course) {
    // remove course
    const courseList = e.currentTarget.parentElement;
    courseList.remove();

    // populate input fields
    courseNameInput.value = course.title;
    courseTypeInput.value = course.type;
    courseDescriptionInput.value = course.description;
    teacherNameInput.value = course.teacher;

    // set id
    formContainer.setAttribute('data-id', course._id);

    // activate edit course button and deactivate add course btn
    activateEditButton();
}

function sendChange() {
    // get inputs
    const newCourse = getInputData();

    // get course id
    const courseId = formContainer.getAttribute('data-id');

    // remove form id attribute
    formContainer.removeAttribute('data-id');

    // send put request
    if (newCourse) {
        fetch(`${baseUrl}/${courseId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ courseId, ...newCourse })
        })
            .then(response => {
                if (!response.ok) {
                    return;
                }
                // clear inputs
                clearAllInputs();
                // activate add and deactivate edit
                activateAddButton();
                // load courses
                return loadCourses();
            })
    }
}

function finishCourse(e) {
    // get target course
    const courseToRemove = e.currentTarget.parentElement;

    // get course id
    const courseId = courseToRemove.getAttribute('data-id');

    // send delete request
    fetch(`${baseUrl}/${courseId}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (!response.ok) {
            return;
        }
        // remove course
        courseToRemove.remove();
        // fetch items
        // return loadCourses();
    })
}