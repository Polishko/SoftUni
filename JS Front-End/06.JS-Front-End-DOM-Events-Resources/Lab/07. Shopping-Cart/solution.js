function solve() {
   let divCollection = document.querySelectorAll('.product > *'); // All relevant divs collected
   let textarea = document.querySelector('textarea'); // The area to be filled retrieved
   let products = []; // The products purchased
   let totalCost = 0;
   let checkOutButton = document.querySelector('.checkout');

   // Creating a list of objects, each object with img, info, button and price attributes; Also adding the click-event listener to the button attribute
   let shoppingList = Array.from(divCollection).reduce((result, divElement, i) => {
      
      const attributes = new Map([
         [0, 'img'],
         [1, 'info'],
         [2, 'button'],
         [3, 'price']
     ]);

     let idx = i % 4;

     if (idx === 0) {
      result.push({}); // Create new object when previous object's attributes and values are retrieved
     }

     // Add the event listener to the button in object
     if (idx === 2) {
      divElement.addEventListener('click', function(e) {
         textarea.disabled = false;
         let associatedObject = result[Math.floor(i / 4)];
         let name =  associatedObject['info'].querySelector('.product-title').textContent;
         let price = Number(associatedObject['price'].textContent);
         textarea.value += `Added ${name} for ${price.toFixed(2)} to the cart.\n`
         totalCost += price;

         if (!products.includes(name)) {
            products.push(name); // Add unique product names
         }

      });
     }

     // Get the current object in the result array and add the div element to the relevant attribute 
     let currentObject = result[result.length - 1];
     currentObject[attributes.get(idx)] = divElement;

     return result; //Accumulate the result array

   }, []);

   // Add the checkout button event listener
   checkOutButton.addEventListener('click', function(e) {
      let list = products.join(', ');
      textarea.value += `You bought ${list} for ${totalCost.toFixed(2)}.`;
      Array.from(document.querySelectorAll('button')).forEach(button => button.setAttribute('disabled', 'true')); // Disable all buttons after checkout
   });

   // return shoppingList;
}

 
