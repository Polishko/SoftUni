function create(words) {
   let mainDiv = document.getElementById('content');

   for (const word of words) {
      const divItem = document.createElement('div');
      const pItem = document.createElement('p');
      pItem.textContent = word;
      pItem.style.display = 'none';

      divItem.appendChild(pItem);

      divItem.addEventListener('click', function(e) {
         pItem.style.display = 'block';
      });

      mainDiv.appendChild(divItem); 
   }

   // or use map on each word with all actions above and return the div then add the event listener to each div. But I think for loop is better, it does all in one cycle.
}
