// Load page content for logged user
document.addEventListener('DOMContentLoaded', function() { //DOMContentLoaded event fired when HTML doc is loaded
    const isLoggedIn = checkUserLoggedIn();

    if (!isLoggedIn) {
        disableAllExceptLoad();
        document.querySelector('nav #logout').style.display = 'none';
    } else {
        const userEmail = sessionStorage.getItem('email');
        document.querySelector('header .email span').textContent = userEmail;
        document.querySelector('nav #login').style.display = 'none';
        document.querySelector('nav #register').style.display = 'none';
    }

    // Hide cactch initially
    document.querySelector('#main').style.display = 'none';
});

function checkUserLoggedIn() {
    return sessionStorage.getItem('isLoggedIn') === 'true'; //localStorage: built-in web API, persistantly store data across sessions
}

function disableAllExceptLoad() {
    const disableButtons = document.querySelectorAll('button:not(.load)');
    disableButtons.forEach(button => {
        button.disabled = true;
    });
}

// Logout logic
const logoutButton = document.getElementById('logout');

logoutButton.addEventListener('click', async (event) => {
    event.preventDefault();

    try {
        // Logging the token before making the fetch call
        const token = sessionStorage.getItem('token');
        console.log('Authorization Token:', token);

        const response = await fetch('http://localhost:3030/users/logout', {
            method: 'GET',
            headers: { 'X-Authorization': token }
        });

        if (response.status === 204) {
            // Clear session storage and redirect
            sessionStorage.clear();
            window.location.href = 'index.html';
        } else {
            console.error('Logout failed', response.statusText);
        }
        
    } catch (error) {
        console.error('Error during logout:', error)
    }
});

// Event listener for the Load button
const loadButton = document.querySelector('button.load');
loadButton.addEventListener('click', async () => {
    try {
        const response = await fetch('http://localhost:3030/data/catches');
        if (response.ok) {
            const catches = await response.json();
            console.log(catches)
            renderCatches(catches);
        } else {
            console.error('Failed to load catches:', response.statusText);
        }
    } catch (error) {
        console.error('Error loading catches:', error);
    }
});

// Function to get user details
async function getUserDetails() {
    try {
        const token = sessionStorage.getItem('token'); // Get the session token
        if (!token) {
            console.error('No token found');
            return null; // Return null if token is not found
        }

        const response = await fetch('http://localhost:3030/users/me', {
            method: 'GET',
            headers: { 'X-Authorization': token }
        });

        if (response.ok) {
            const userData = await response.json();
            // console.log('User Details:', userData);
            return userData._id; // Return the _id of the user
        } else {
            console.error('Failed to fetch user details:', response.status);
            return null; // Return null if there's an error
        }
    } catch (error) {
        console.error('Error fetching user details:', error);
        return null; // Return null if there's an error
    }
}

// Call the function to get user details
const userId = await getUserDetails();

// Rendering Catches
function renderCatches(catches) {   
    const catchesContainer = document.getElementById('catches');
    catchesContainer.innerHTML = ''; // Clear previous catches

    catches.forEach(catchItem => {
        const catchDiv = document.createElement('div');
        catchDiv.className = 'catch';

        // Render catch details (angler, weight, species, etc.)
        const anglerLabel = document.createElement('label');
        anglerLabel.textContent = 'Angler';
        catchDiv.appendChild(anglerLabel);
        const anglerInput = document.createElement('input');
        anglerInput.type = 'text';
        anglerInput.className = 'angler';
        anglerInput.value = catchItem.angler;
        catchDiv.appendChild(anglerInput);

        const weightLabel = document.createElement('label');
        weightLabel.textContent = 'Weight';
        catchDiv.appendChild(weightLabel);
        const weightInput = document.createElement('input');
        weightInput.type = 'text';
        weightInput.className = 'weight';
        weightInput.value = catchItem.weight;
        catchDiv.appendChild(weightInput);

        const speciesLabel = document.createElement('label');
        speciesLabel.textContent = 'Species';
        catchDiv.appendChild(speciesLabel);
        const speciesInput = document.createElement('input');
        speciesInput.type = 'text';
        speciesInput.className = 'species';
        speciesInput.value = catchItem.species;
        catchDiv.appendChild(speciesInput);

        const locationLabel = document.createElement('label');
        locationLabel.textContent = 'Location';
        catchDiv.appendChild(locationLabel);
        const locationInput = document.createElement('input');
        locationInput.type = 'text';
        locationInput.className = 'location';
        locationInput.value = catchItem.location;
        catchDiv.appendChild(locationInput);

        const baitLabel = document.createElement('label');
        baitLabel.textContent = 'Bait';
        catchDiv.appendChild(baitLabel);
        const baitInput = document.createElement('input');
        baitInput.type = 'text';
        baitInput.className = 'bait';
        baitInput.value = catchItem.bait;
        catchDiv.appendChild(baitInput);

        const captureTimeLabel = document.createElement('label');
        captureTimeLabel.textContent = 'Capture Time';
        catchDiv.appendChild(captureTimeLabel);
        const captureTimeInput = document.createElement('input');
        captureTimeInput.type = 'text';
        captureTimeInput.className = 'captureTime';
        captureTimeInput.value = catchItem.captureTime;
        catchDiv.appendChild(captureTimeInput);

        // Render update and delete buttons
        const updateButton = document.createElement('button');
        updateButton.className = 'update';
        updateButton.setAttribute('data-id', catchItem._id);
        updateButton.textContent = 'Update';
        catchDiv.appendChild(updateButton);

        const deleteButton = document.createElement('button');
        deleteButton.className = 'delete';
        deleteButton.setAttribute('data-id', catchItem._id);
        deleteButton.textContent = 'Delete';
        catchDiv.appendChild(deleteButton);

        catchesContainer.appendChild(catchDiv);

        // Determine if the current user is the creator of this catch
        const isCurrentUserCatch = catchItem._ownerId === userId;
        console.log(catchItem._ownerId)
        console.log(isCurrentUserCatch)

        if (!isCurrentUserCatch) {
            // Disable update and delete buttons if the current user is not the creator
            updateButton.disabled = true;
            deleteButton.disabled = true;
        }
        // Event listener for update button
        updateButton.addEventListener('click', async () => {
            try {
                const token = sessionStorage.getItem('token');
                const response = await fetch(`http://localhost:3030/data/catches/${catchItem._id}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Authorization': token
                    },
                    body: JSON.stringify({
                        angler: anglerInput.value,
                        // Repeat for other input fields...
                    })
                });
                if (response.ok) {
                    // Catch updated successfully
                    console.log('Catch updated successfully');
                } else {
                    console.error('Failed to update catch:', response.statusText);
                }
            } catch (error) {
                console.error('Error updating catch:', error);
            }
        });

        // Event listener for delete button
        deleteButton.addEventListener('click', async () => {
            try {
                const token = sessionStorage.getItem('token');
                const response = await fetch(`http://localhost:3030/data/catches/${catchItem._id}`, {
                    method: 'DELETE',
                    headers: {
                        'X-Authorization': token
                    }
                });
                if (response.ok) {
                    // Catch deleted successfully
                    console.log('Catch deleted successfully');
                    catchesContainer.removeChild(catchDiv); // Remove the catch from UI
                } else {
                    console.error('Failed to delete catch:', response.statusText);
                }
            } catch (error) {
                console.error('Error deleting catch:', error);
            }
        });
    });

    document.querySelector('#main').style.display = 'inline-block';
}


updateButton.addEventListener('click', async () => {
    try {
        const token = sessionStorage.getItem('token');
        const response = await fetch(`http://localhost:3030/data/catches/${catchItem._id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': token
            },
            body: JSON.stringify({
                angler: anglerInput.value,
                weight: weightInput.value,
                species: speciesInput.value,
                location: locationInput.value,
                bait: baitInput.value,
                captureTime: captureTimeInput.value
            })
        });
        if (response.ok) {
            // Catch updated successfully
            console.log('Catch updated successfully');
        } else {
            console.error('Failed to update catch:', response.statusText);
        }
    } catch (error) {
        console.error('Error updating catch:', error);
    }
});

// Delete a catch
catchDiv.appendChild(deleteButton);
deleteButton.addEventListener('click', async () => {
    try {
        const token = sessionStorage.getItem('token');
        const response = await fetch(`http://localhost:3030/data/catches/${catchItem._id}`, {
            method: 'DELETE',
            headers: {
                'X-Authorization': token
            }
        });
        if (response.ok) {
            // Catch deleted successfully
            console.log('Catch deleted successfully');
            catchesContainer.removeChild(catchDiv); // Remove the catch from UI
        } else {
            console.error('Failed to delete catch:', response.statusText);
        }
    } catch (error) {
        console.error('Error deleting catch:', error);
    }
});

// Add a catch
const addButton = document.getElementById('add');
addButton.addEventListener('click', async () => {
    try {
        const token = sessionStorage.getItem('token');
        const angler = document.getElementById('addAngler').value;
        const weight = document.getElementById('addWeight').value;
        const species = document.getElementById('addSpecies').value;
        const location = document.getElementById('addLocation').value;
        const bait = document.getElementById('addBait').value;
        const captureTime = document.getElementById('addCaptureTime').value;

        const response = await fetch('http://localhost:3030/data/catches', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Authorization': token
            },
            body: JSON.stringify({
                angler,
                weight,
                species,
                location,
                bait,
                captureTime
            })
        });
        if (response.ok) {
            // Catch added successfully
            console.log('Catch added successfully');
            const newCatch = await response.json();
            renderNewCatch(newCatch); // Render the newly added catch
        } else {
            console.error('Failed to add catch:', response.statusText);
        }
    } catch (error) {
        console.error('Error adding catch:', error);
    }
});

// Function to render a newly added catch
function renderNewCatch(newCatch) {
    const catchDiv = document.createElement('div');
    catchDiv.className = 'catch';

    // Render catch details
    const anglerLabel = document.createElement('label');
    anglerLabel.textContent = 'Angler';
    catchDiv.appendChild(anglerLabel);
    const anglerInput = document.createElement('input');
    anglerInput.type = 'text';
    anglerInput.className = 'angler';
    anglerInput.value = newCatch.angler;
    catchDiv.appendChild(anglerInput);

    const weightLabel = document.createElement('label');
    weightLabel.textContent = 'Weight';
    catchDiv.appendChild(weightLabel);
    const weightInput = document.createElement('input');
    weightInput.type = 'text';
    weightInput.className = 'weight';
    weightInput.value = newCatch.weight;
    catchDiv.appendChild(weightInput);

    const speciesLabel = document.createElement('label');
    speciesLabel.textContent = 'Species';
    catchDiv.appendChild(speciesLabel);
    const speciesInput = document.createElement('input');
    speciesInput.type = 'text';
    speciesInput.className = 'species';
    speciesInput.value = newCatch.species;
    catchDiv.appendChild(speciesInput);

    const locationLabel = document.createElement('label');
    locationLabel.textContent = 'Location';
    catchDiv.appendChild(locationLabel);
    const locationInput = document.createElement('input');
    locationInput.type = 'text';
    locationInput.className = 'location';
    locationInput.value = newCatch.location;
    catchDiv.appendChild(locationInput);

    const baitLabel = document.createElement('label');
    baitLabel.textContent = 'Bait';
    catchDiv.appendChild(baitLabel);
    const baitInput = document.createElement('input');
    baitInput.type = 'text';
    baitInput.className = 'bait';
    baitInput.value = newCatch.bait;
    catchDiv.appendChild(baitInput);

    const captureTimeLabel = document.createElement('label');
    captureTimeLabel.textContent = 'Capture Time';
    catchDiv.appendChild(captureTimeLabel);
    const captureTimeInput = document.createElement('input');
    captureTimeInput.type = 'text';
    captureTimeInput.className = 'captureTime';
    captureTimeInput.value = newCatch.captureTime;
    catchDiv.appendChild(captureTimeInput);

    // Render update and delete buttons
    const updateButton = document.createElement('button');
    updateButton.className = 'update';
    updateButton.setAttribute('data-id', newCatch._id);
    updateButton.textContent = 'Update';
    catchDiv.appendChild(updateButton);

    const deleteButton = document.createElement('button');
    deleteButton.className = 'delete';
    deleteButton.setAttribute('data-id', newCatch._id);
    deleteButton.textContent = 'Delete';
    catchDiv.appendChild(deleteButton);

    catchesContainer.appendChild(catchDiv);    
}
