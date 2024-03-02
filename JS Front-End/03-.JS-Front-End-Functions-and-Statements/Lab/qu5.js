function calculator(num1, num2, operator) {
    let operations = {
        'multiply': () => num1 * num2,
        'divide': () => num1 / num2,
        'add': () => num1 + num2,
        'subtract': () => num1 - num2,
    }

    let result = operations[operator] ();
    console.log(result);
}

// calculator(5, 5, 'multiply');
// calculator(40, 8, 'divide');
// calculator(12, 19, 'add');
// calculator(50, 13, 'subtract');
