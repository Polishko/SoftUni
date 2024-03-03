function oddEvenSum(num) {
    let oddNums = num.toString().split('').filter(oddNum => oddNum % 2 !== 0);
    let evenNums = num.toString().split('').filter(evenNum => evenNum % 2 === 0);
    let sumOddNums = oddNums.reduce((acc, curr) => acc + parseInt(curr), 0);
    let sumEvenNums = evenNums.reduce((acc, curr) => acc + parseInt(curr), 0);

    return `Odd sum = ${sumOddNums}, Even sum = ${sumEvenNums}`;
}

// console.log(oddEvenSum(1000435));
// console.log(oddEvenSum(3495892137259234));
