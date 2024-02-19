function solve(num1, num2, operator) {
    const expression = `${num1} ${operator} ${num2}`;
    console.log(eval(expression))
}

solve(0, 0, '/')