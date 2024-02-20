function fruits(fruit, weight, money) {
    let totalMoney = money * weight / 1000
    let weightKilograms = weight / 1000
    console.log(`I need \$${totalMoney.toFixed(2)} to buy ${weightKilograms.toFixed(2)} kilograms ${fruit}.`);
}

// fruits('orange', 2500, 1.80);
// fruits('apple', 1563, 2.35);