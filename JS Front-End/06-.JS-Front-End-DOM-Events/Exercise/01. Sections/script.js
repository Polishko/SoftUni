function create(words) {
   let mainDiv = document.getElementById('content');

   for (const word of words) {
      let divItem = document.createElement('div');
      let pItem = document.createElement('p');
      pItem.textContent = word;
      pItem.style.display = 'none';

      divItem.appendChild(pItem);

      divItem.addEventListener('click', function(e) {
         pItem.style.display = 'block';
      });

      mainDiv.appendChild(divItem); 
   }
}