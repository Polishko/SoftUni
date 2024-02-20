
function digitSum(num) {
    let sumTotal = 0;
    let remainder = 0;

    while (num > 0) {
        remainder = num % 10;
        sumTotal += remainder;
        num = Math.floor(num / 10);
    }

    console.log(sumTotal);
    
}



// function digitSum(num) {
//     let sumTotal = 0;

//     for (let digit of num.toString()) {
//         sumTotal += parseInt(digit, 10);
//     }

//     console.log(sumTotal);
// }


// digitSum(97561);