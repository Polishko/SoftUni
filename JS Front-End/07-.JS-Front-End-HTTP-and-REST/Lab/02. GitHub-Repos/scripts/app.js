function loadRepos() {
   fetch('https://api.github.com/users/testnakov/repos')
   .then((response) => response.text())
   .then((data) => {
      document.getElementById('res').textContent = data;
   })
   .catch((error) => {
      console.error('Error loading repositories:', error);
  });
}