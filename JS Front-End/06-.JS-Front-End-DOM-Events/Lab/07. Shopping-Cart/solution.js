function solve() {
   let divCollection = document.querySelectorAll('.product > *'); // All relevant divs
   let textarea = document.querySelector('textarea'); // The area to be filled
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
      result.push({}); // Create a new object after previous object's all attributes and values (div's) are retrieved
     }

     // Add the event listener to the button div in the object
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

     // Update the current object in the result array with the current div element 
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

 
