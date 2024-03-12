function createCatalogue(inputArray) {
    let products = {};

    for (info of inputArray) {
        let product = {};
        const [name, price] = info.split(' : ');
        const keyMain = name[0];
        product[name] = price;
        

        if (!products.hasOwnProperty(keyMain)) {
            products[keyMain] = []; 
        }

        products[keyMain].push(product);
    }

    const sortedProducts = Object.entries(products).sort((a, b) => a[0].localeCompare(b[0]));

    for (let [letter, productList] of sortedProducts) {
        console.log(letter);

        const sortedList = productList.sort((a, b) => {
            const keyA = Object.keys(a)[0];
            const keyB = Object.keys(b)[0];
            
            return keyA.localeCompare(keyB);
    });
        for (let item of sortedList) {
            const itemName = Object.keys(item)[0];
            const itemValue = item[itemName];
            console.log(`  ${itemName}: ${itemValue}`)
        }    
    }
}

// createCatalogue([
//     'Appricot : 20.4',
//     'Fridge : 1500',
//     'TV : 1499',
//     'Deodorant : 10',
//     'Boiler : 300',
//     'Apple : 1.25',
//     'Anti-Bug Spray : 15',
//     'T-Shirt : 10'
//     ]
//     );

// createCatalogue([
//     'Omlet : 5.4',
//     'Shirt : 15',
//     'Cake : 59'
//     ]
//     );