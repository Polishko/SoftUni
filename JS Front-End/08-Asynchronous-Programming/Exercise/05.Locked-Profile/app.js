function lockedProfile() {
    function createProfileCard(dataKey, num) {
        const fragment = document.createDocumentFragment();
        // Main div
        const profileDiv = document.createElement('div');
        profileDiv.className = 'profile';
        // img
        const imgEle = document.createElement('img');
        imgEle.src = './iconProfile2.png';
        imgEle.className = 'userIcon';
        profileDiv.appendChild(imgEle);
        // lock unlock form
        const lockLabel = document.createElement('label');
        lockLabel.textContent = 'Lock';
        profileDiv.appendChild(lockLabel);
        
        const inputLock = document.createElement('input');
        inputLock.type = 'radio';
        inputLock.name = `user${num}Locked`;
        inputLock.value = 'lock';
        inputLock.checked = true;
        profileDiv.appendChild(inputLock);

        const unlockLabel = document.createElement('label');
        unlockLabel.textContent = 'Unlock';
        profileDiv.appendChild(unlockLabel);

        const inputUnlock = document.createElement('input');
        inputUnlock.type = 'radio';
        inputUnlock.name = `user${num}Locked`;
        inputUnlock.value = 'unlock';
        profileDiv.appendChild(inputUnlock);
        // br hr elements
        const brEle = document.createElement('br');
        profileDiv.appendChild(brEle);
        const hr1 = document.createElement('hr');
        profileDiv.appendChild(hr1);
        // Username form
        const userLabel = document.createElement('label');
        userLabel.textContent = 'Username';
        profileDiv.appendChild(userLabel);
        const inputUserName = document.createElement('input');
        inputUserName.type = 'text';
        inputUserName.name = `user${num}Username`;
        inputUserName.value = dataKey.username;
        inputUserName.setAttribute('disabled', 'true');
        inputUserName.setAttribute('readonly', 'true');
        profileDiv.appendChild(inputUserName);
        // Email Age User Div
        const userDiv = document.createElement('div');
        userDiv.className = 'hiddenInfo';
        const hr2 = document.createElement('hr');
        userDiv.appendChild(hr2);
        // Email form
        const emailLabel = document.createElement('label');
        emailLabel.textContent = 'Email:';
        userDiv.appendChild(emailLabel);
        const inputEmail = document.createElement('input');
        inputEmail.type = 'email';
        inputEmail.name = `user${num}Email`;
        inputEmail.value = dataKey.email;
        inputEmail.setAttribute('disabled', 'true');
        inputEmail.setAttribute('readonly', 'true');
        userDiv.appendChild(inputEmail);
        // Age form
        const ageLabel = document.createElement('label');
        ageLabel.textContent = 'Age:';
        userDiv.appendChild(ageLabel);
        const inputAge = document.createElement('input');
        inputAge.type = 'email'; // Judge tests this as email because thats how its defined in the problem
        inputAge.name = `user${num}Age`;
        inputAge.value = dataKey.age;
        inputAge.setAttribute('disabled', 'true');
        inputAge.setAttribute('readonly', 'true');
        userDiv.appendChild(inputAge);
        // Append Email Age div
        profileDiv.appendChild(userDiv);
        // Add button
        const buttonEle = document.createElement('button');
        buttonEle.textContent = 'Show more';
        profileDiv.appendChild(buttonEle);
        
        // Button event listener
        buttonEle.addEventListener('click', function(e) {       
            if (inputUnlock.checked) {
                if (buttonEle.textContent === 'Show more') {
                    inputEmail.style.display = 'inline-block';
                    emailLabel.style.display = 'inline-block';
                    inputAge.style.display = 'inline-block';
                    ageLabel.style.display = 'inline-block';
                    buttonEle.textContent = 'Hide it';
                } else {
                    inputEmail.style.display = 'none';
                    emailLabel.style.display = 'none';
                    inputAge.style.display = 'none';
                    ageLabel.style.display = 'none';
                    buttonEle.textContent = 'Show more';
                }
            }
        });
        
        fragment.appendChild(profileDiv);

        return fragment;
    }
    
    function createProfiles() {
        const mainEle = document.getElementById('main');
        mainEle.innerHTML = '';

        fetch('http://localhost:3030/jsonstore/advanced/profiles')
        .then((response) => response.json())
        .then((data) => {
            // console.log(data);
            let count = 0;
            for (const key in data) {
                count += 1;
                const profileCard = createProfileCard(data[key], count);
                mainEle.appendChild(profileCard); 
            }
        })
        .catch((error) => error)
    }

    createProfiles();
 
}
