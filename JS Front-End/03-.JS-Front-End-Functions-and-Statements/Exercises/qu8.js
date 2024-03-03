function isPerfectNumber(num) {
    if (num <= 1) {
        console.log(`It's not so perfect.`);
    }

    let sumDivisors = 1;

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            sumDivisors += i;
            if (num / i !== i) {
                sumDivisors += num / i;
            }
        }
    }

    if (sumDivisors === num) {
        console.log(`We have a perfect number!`);
            } else {
                console.log(`It's not so perfect.`);
            }
}

// isPerfectNumber(6);
// isPerfectNumber(28);
// isPerfectNumber(1236498);

// function isPerfectNumber(num) {
//     let allNums = Array.from({length: num - 1}, (_, index) => index + 1);
//     let divisors = allNums.filter(divisor => num % divisor === 0);
//     let sumDivisors = divisors.reduce((acc, curr) => acc + curr, 0);

//     if (sumDivisors === num) {
//         console.log(`We have a perfect number!`);
//     } else {
//         console.log(`It's not so perfect.`);
//     }
// }

// isPerfectNumber(6);
// isPerfectNumber(28);
// isPerfectNumber(1236498);