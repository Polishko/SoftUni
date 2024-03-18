let digits = [];
let option = 'Hexadecimal';
// let option = 'Decimal';


const divisor = (option === 'Hexadecimal') ? 16 : 2;

const convertNum = (num) => {
    let quotient = parseInt(num / divisor);
    let remainder = num % divisor;

    if (quotient === 0) {
        digits.push(remainder);
        return digits.reverse().join('');
    }

    if (option === 'Hexadecimal' && remainder >= 12) {
        const letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'D'};
        remainder = letters[remainder];
    }

    digits.push(remainder);
    return convertNum(quotient);
    }

// console.log(convertNum(960));
// console.log(convertNum(8));
console.log(convertNum(140));