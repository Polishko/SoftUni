function lockedProfile() {
    allButtons = document.querySelectorAll('button');

    Array.from(allButtons).forEach(button => {
        button.addEventListener('click', function(e) {
            const parentDiv = button.parentElement;
            const lock = parentDiv.querySelector('input[value=lock]');

            if (button.textContent === 'Show more') {
                if (lock.checked === false) {     
                    button.parentElement.querySelector('[id*=HiddenFields]').style.display = 'block';           
                    button.textContent = 'Hide it';
                }
            } else {
                if (lock.checked === false) {
                    button.parentElement.querySelector('[id*=HiddenFields]').style.display = 'none';  
                    button.textContent = 'Show more';
                }
            }    
        });
    });
}