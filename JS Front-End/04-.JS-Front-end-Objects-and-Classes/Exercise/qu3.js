function updateProducts(stockArray, orderArray) {

    function addItems(objectItems, listItems) {
        for (let i = 0; i < listItems.length; i+=2) {
            const item = listItems[i];
            const quantity = parseInt(listItems[i + 1]);

            if (!(item in objectItems)) {
                objectItems[item] = 0;
            }

            objectItems[item] += quantity;
        }
    }
        
    let products = {};
    addItems(products, stockArray);
    addItems(products, orderArray);

    Object.entries(products).forEach((entry) => console.log(`${entry[0]} -> ${entry[1]}`));

    }


// updateProducts([
//     'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
//     ],
//     [
//     'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
//     ]
//     );

// updateProducts([
//     'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
//     ],
//     [
//     'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
//     ]
//     );
