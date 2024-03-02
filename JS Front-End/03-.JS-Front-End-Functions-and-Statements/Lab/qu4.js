function calculateOrder(product, amount) {
    let price = 0;
    switch (product) {
        case 'coffee':
            price = 1.5;
            break;
        case 'water':
            price = 1.00;
            break;
        case 'coke':
            price = 1.40;
            break;
        case 'snacks':
            price = 2.00   
            break;
    }

    console.log((price * amount).toFixed(2));
}

// calculateOrder('water', 5);
// calculateOrder('coffee', 2);