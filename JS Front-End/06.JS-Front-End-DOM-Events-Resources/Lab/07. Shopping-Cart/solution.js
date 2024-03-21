function solve() {
   let divCollection = document.querySelectorAll('.product > *');
   let textarea = document.querySelector('textarea');
   let products = [];
   let totalCost = 0;
   let checkOutButton = document.querySelector('.checkout');
   
   let shoppingList = Array.from(divCollection).reduce((result, divElement, i) => {
      
      const attributes = new Map([
         [0, 'img'],
         [1, 'info'],
         [2, 'button'],
         [3, 'price']
     ]);

     let idx = i % 4;

     if (idx === 0) {
      result.push({});
     }

     if (idx === 2) {
      divElement.addEventListener('click', function(e) {
         textarea.disabled = false;
         let target = e.currentTarget;
         let associatedObject = result[Math.floor(i / 4)];
         let name =  associatedObject['info'].querySelector('.product-title').textContent;
         let price = Number(associatedObject['price'].textContent);
         textarea.value += `Added ${name} for ${price.toFixed(2)} to the cart.\n`
         totalCost += price;

         if (!products.includes(name)) {
            products.push(name);
         }

      });
     }


     let currentObject = result[result.length - 1];
     currentObject[attributes.get(idx)] = divElement;

     return result;

   }, []);

   checkOutButton.addEventListener('click', function(e) {
      let list = products.join(', ');
      textarea.value += `You bought ${list} for ${totalCost.toFixed(2)}.`;
      Array.from(document.querySelectorAll('button')).forEach(button => button.setAttribute('disabled', 'true'));
   });

   // return shoppingList;
}

 