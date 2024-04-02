document.querySelector('nav #home').classList.remove('active');
document.querySelector('nav #logout').style.display = 'none';
// document.querySelector('nav #login').classList.remove('active');
// document.querySelector('nav #logout').classList.add('active');

const registerForm = document.querySelector('form#register');

registerForm.addEventListener('submit', async (event) => {
    event.preventDefault();
     const email = registerForm.querySelector('input[name="email"]').value;
     const password = registerForm.querySelector('input[name="password"]').value;
     const rePassword = registerForm.querySelector('input[name="rePass"]').value;

     if (!password || !email || !rePassword)  {
        displayErrorMessage('Please fill in all fields');
        return;
     }

     if (password !== rePassword) {
        displayErrorMessage('Passwords do not match');
        return;
     }

     try {
        const response = await fetch('http://localhost:3030/users/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            window.location.href = 'index.html';
        } else {
            const errorMessage = await response.text();
            displayErrorMessage(errorMessage);
        }
     } catch (error) {
        console.error('Error during registration:', error);
        displayErrorMessage('An error occurred. Please try again later.');
     }
})

function displayErrorMessage(message) {
    const notification = registerForm.querySelector('.notification');
    notification.textContent = message;
}