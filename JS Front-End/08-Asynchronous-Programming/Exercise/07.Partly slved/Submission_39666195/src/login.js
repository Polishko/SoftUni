document.querySelector('nav #home').classList.remove('active');
document.querySelector('nav #logout').style.display = 'none';
document.querySelector('nav #login').classList.add('active');

const loginForm = document.querySelector('form#login');
const loginButton = loginForm.querySelector('button')

loginForm.addEventListener('submit', async (event) => { //Event listener on form also catches pressing Enter; async returns a Promise
    event.preventDefault(); // Preventing default submission behavior to allow implementing login logic

    const email = loginForm.querySelector('input[name="email"]').value;
    const password = loginForm.querySelector('input[name="password"]').value;

    await loginUser(email, password); // await waits the Promise to resolve, pauses async execution till Promise is resolved
})

async function loginUser(email, password) {
    try {
        const response = await fetch('http://localhost:3030/users/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });
        if (response.ok) {
            const responseData = await response.json();
            // console.log(responseData);
            // Store user login session
            sessionStorage.setItem('isLoggedIn', 'true');
            // console.log('User email:', email);
            sessionStorage.setItem('email', email);

            const token = responseData.accessToken;
            // console.log(token)
            sessionStorage.setItem('token', token);
            window.location.href = 'index.html';
        } else {
            // Display error message
            const errorMessage = await response.text();
            console.error(errorMessage);
            // Display error message to user
            const notification = document.querySelector('#login-view .notification');
            notification.textContent = errorMessage;
        }
    } catch (error) {
        console.error('Error during login:', error);
    }
}