function attachEvents() {
  BASE_URL = 'http://localhost:3030/jsonstore/collections/students';
  const submitButton = document.getElementById('submit');
  const tableBody = document.querySelector('#results tbody');
  let allStudents;

  const populateTable = function(data) {
    allStudents = Object.entries(data);
      for (const student of allStudents) { 
        const rowElement = document.createElement('tr');

        const firstNameCol = document.createElement('td')
        firstNameCol.textContent = student[1].firstName;
        const lastNameCol = document.createElement('td')
        lastNameCol.textContent = student[1].lastName;
        const facultyNumCol = document.createElement('td')
        facultyNumCol.textContent = student[1].facultyNumber;
        const gradeCol = document.createElement('td')
        gradeCol.textContent = student[1].grade;

        rowElement.appendChild(firstNameCol);
        rowElement.appendChild(lastNameCol);
        rowElement.appendChild(facultyNumCol);
        rowElement.appendChild(gradeCol);

        tableBody.appendChild(rowElement);
      }
  };

  const createStundent = function() {
    const firstNameInput = document.querySelector('.inputs input[name="firstName"]');
    const lastNameInput = document.querySelector('.inputs input[name="lastName"]');
    const facultyNumInput = document.querySelector('.inputs input[name="facultyNumber"]');
    const gradeInput = document.querySelector('.inputs input[name="grade"]');

    const newStudent = {
      firstName: firstNameInput.value,
      lastName: lastNameInput.value,
      facultyNumber: facultyNumInput.value,
      grade: gradeInput.value,
    };

    fetch(BASE_URL, {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify(newStudent),
    })
    .then((response) => response.json())
    .then(loadStudents)
    .catch((error) => console.log(error.message))

    firstNameInput.value = '';
    lastNameInput.value = '';
    facultyNumInput.value = '';
    gradeInput.value = '';

  };

  const loadStudents = function () {
    tableBody.innerHTML = '';
    fetch(BASE_URL)
    .then((response) => response.json())
    .then((data) => {
      // console.log(data);
      populateTable(data);
      
      
    })
    .catch((error) => console.log(error.message))
  };

  submitButton.addEventListener('click', createStundent)
  loadStudents(); // Even though not clearly stated in the problem, info should load before any new student is added

}

attachEvents();