function solution() {
    const BASE_URL = 'http://localhost:3030/jsonstore/advanced/articles/';
    const mainSection = document.getElementById('main');

    // Load content
    fetch(`${BASE_URL}list`)
    .then((response) => response.json())
    .then((data) => {
        // console.log(data);
        //Load visible content
        data.forEach(obj => {
            const articleDiv = document.createElement('div');
            articleDiv.className = 'accordion'; 
            const headDiv = document.createElement('div');
            headDiv.className = 'head';
            headSpan = document.createElement('span');
            headSpan.textContent = obj.title;
            headDiv.appendChild(headSpan);
            const button = document.createElement('button');
            button.className = 'button';
            button.id = obj._id;
            button.textContent = 'More';
            button.style.font = 'uppercase'; 
            button.style.fontWeight = 'bold';
            headDiv.appendChild(button);
            articleDiv.appendChild(headDiv);
            mainSection.appendChild(articleDiv);

            // Load hidden content
            fetch(`${BASE_URL}details/${button.id}`)
                .then((response) => response.json())
                .then((data) => {
                    // console.log(data);
                    const extraDiv = document.createElement('div');
                    extraDiv.className = 'extra';
                    const contentP = document.createElement('p');
                    contentP.textContent = data.content;
                    extraDiv.appendChild(contentP);
                    articleDiv.appendChild(extraDiv);
                })
                .catch((error) => console.log(error.message))
            
            // Add button event listener
            button.addEventListener('click', function(e) {
                const hiddenDiv = document.querySelector('.extra')
                if (button.textContent === 'More') {
                    hiddenDiv.style.display = 'block';
                    button.textContent = 'Less';
                } else {
                    hiddenDiv.style.display = 'none';
                    button.textContent = 'More';
                }         
            });
        })    
    })
    .catch((error) => console.log(error.message))
}

solution();
