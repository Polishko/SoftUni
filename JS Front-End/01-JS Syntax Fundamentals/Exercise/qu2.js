function calculatePrice (sizeGroup, typeGroup, weekDay) {
    const priceClasses = {
        'Students': {
            'Friday': 8.45,
            'Saturday': 9.80,
            'Sunday': 10.46,
        },
        'Business': {
            'Friday': 10.90,
            'Saturday': 15.60,
            'Sunday': 16,
        },
        'Regular': {
            'Friday': 15,
            'Saturday': 20,
            'Sunday': 22.50,
        },
    };

    let unitPrice = priceClasses[typeGroup][weekDay];
    let finalPrice;

    switch (typeGroup) {
        case 'Students':
            if (sizeGroup >= 30) {
                unitPrice *= 0.85;
            }
            break;
        case 'Business': {
            if (sizeGroup >= 100) {
                sizeGroup -= 10;
            }
        }
        break;

        case 'Regular': {
            if (sizeGroup >= 10 && sizeGroup <= 20) {
                unitPrice *= 0.95;
            }
        }
        break;
    }

    finalPrice = unitPrice * sizeGroup;
    console.log(`Total price: ${finalPrice.toFixed(2)}`);
}

// calculatePrice(100, 'Business', 'Saturday')