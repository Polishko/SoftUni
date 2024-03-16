function search() {
   const input = document.getElementById('searchText').value;
   const listItems = document.querySelectorAll('#towns li');
   const pattern = new RegExp(`.*(${input}).*`);

   let counter = 0;
   for (let item of listItems) {
      const match = pattern.test(item.textContent);

      if (match) {
         item.style.textDecoration = 'underline';
         item.style.fontWeight = 'bold';
         counter += 1;
      }
   }
   document.getElementById('result').textContent = `${counter} matches found`;
}
