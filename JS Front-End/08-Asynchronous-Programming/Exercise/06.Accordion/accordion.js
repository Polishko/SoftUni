function solution() {
    const BASE_ERL = 'http://localhost:3030/jsonstore/advanced/articles/';
    const mainSection = document.getElementById('main');

    // Load headings
    fetch(`${BASE_ERL}list`)
    .then((response) => response.json())
    .then((data) => {
        // console.log(data);
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

            fetch(`${BASE_ERL}details/${button.id}`)
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

// <!-- <div class="accordion">
// <div class="head">
//     <span>Scalable Vector Graphics</span>
//     <button class="button" id="ee9823ab-c3e8-4a14-b998-8c22ec246bd3">More</button>
// </div>
// <div class="extra">
//     <p>Scalable Vector Graphics .....</p>
// </div>
// </div> -->