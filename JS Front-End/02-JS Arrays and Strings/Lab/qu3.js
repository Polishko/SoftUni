function differenceEvenOdd(myArray) {
    let result = myArray.reduce((sum, num) => num % 2 === 0 ? sum + num : sum - num, 0);
    console.log(result);
}

// function differenceEvenOdd(myArray) {
//     let evenNums = myArray.filter(num => num % 2 === 0);
//     let oddNums = myArray.filter(num => num % 2 !== 0);

//     let evenSum = evenNums.reduce((acc, curr) => acc + curr, 0);
//     let oddSum = oddNums.reduce((acc, curr) => acc + curr, 0);
    
//     console.log(evenSum - oddSum);
// }

// function differenceEvenOdd(myArray) {
//     let evenSum = 0;
//     let oddSum = 0;

//     for (i=0; i<myArray.length; i++) {
//         let current = myArray[i]
//         if (current % 2 === 0) {
//             evenSum += current;
//         } else {
//             oddSum += current;
//         }
//     }

//     console.log(evenSum - oddSum);
// }

// differenceEvenOdd([1,2,3,4,5,6]);
// differenceEvenOdd([3,5,7,9]);
// differenceEvenOdd([2,4,6,8,10]);
