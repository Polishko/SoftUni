function divideFactorials(num1, num2) {
    let findFactorial = function(num) {
        let result = Array.from({length: num}, (_, index) => index + 1).reduce((acc, curr) => acc * curr, 1);
        
        return result;
    }

    let finalResult = findFactorial(num1) / findFactorial(num2);
    console.log(finalResult.toFixed(2));
}

// divideFactorials(5, 2);
// divideFactorials(6, 2);

// function divideFactorials(num1, num2) {
//     let findFactorial = function(num) {
//         let result = 1;

//         if (num !== 1) {
//             for (let i = 2; i <= num; i++) {
//                 result *= i;               
//             }
//         }
        
//         return result;
//     }

//     let finalResult = findFactorial(num1) / findFactorial(num2);
//     console.log(finalResult.toFixed(2));
// }

// divideFactorials(5, 2);
// divideFactorials(6, 2);

// function divideFactorials(num1, num2) {
//     let findFactorial = function(num) {
//         if (num === 1) {
//             return 1;
//         } else {
//             return num * findFactorial(num - 1);
//         }
//     };

//     let result = findFactorial(num1) / findFactorial(num2);
//     console.log(result.toFixed(2));
// }

// divideFactorials(5, 2);
// divideFactorials(6, 2);
