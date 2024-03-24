function loadCommits() {
    const username = document.querySelector('#username').value;
    const repository = document.querySelector('#repo').value;
    const commitList = document.querySelector('#commits');
    commitList.innerHTML = '';

    fetch(`https://api.github.com/repos/${username}/${repository}/commits`)
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Error: ${response.status} (Not Found)`);
        }
        return response.json();
		
    })
    .then((data) => {
        data.forEach((result) => {
            const authorName = result.commit.author.name;
            const commitMessage = result.commit.message;
            let liElement = document.createElement('li');
            liElement.textContent = `${authorName}: ${commitMessage}`;
            commitList.appendChild(liElement);
        });
    })
    .catch((error) => {
		let liElement = document.createElement('li');
		liElement.textContent = error.message;
		commitList.appendChild(liElement);
	})
}