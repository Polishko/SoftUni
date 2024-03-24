function loadRepos() {

	const userID = document.querySelector('#username').value;
	let reposList = document.querySelector('#repos');
	
	while (reposList.firstChild) {
		reposList.removeChild(reposList.firstChild);
	}

	// or reposList.innerHTML = '';

	fetch(`https://api.github.com/users/${userID}/repos`)
	.then((response) => {
		if (!response.ok) {
			throw new Error('User not found or other error occurred.');
		}
		return response.json();
	})
	.then((data) => {
		data.forEach((repo) => {
			const name = repo.full_name;
			const address = repo.html_url;
			let anchorElement = document.createElement('a');
			let liElement = document.createElement('li');
			anchorElement.href = address;
			anchorElement.textContent = name;
			liElement.appendChild(anchorElement);
			reposList.appendChild(liElement);
		});
	})
	.catch((error) => {
		let liElement = document.createElement('li');
		liElement.textContent = error.message;
		reposList.appendChild(liElement);
	})
}