function calculate(num1, operator, num2) {
    const operations = {
        '+': () => num1 + num2,
        '-': () => num1 - num2,
        '/': () => num1 / num2,
        '*': () => num1 * num2,
    };

    let result = operations[operator]();

    console.log(result.toFixed(2));
}

// calculate(5,'+',10);
// calculate(25.5,'-',3);