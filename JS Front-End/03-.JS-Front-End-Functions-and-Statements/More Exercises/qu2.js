function numberMofidy(num) {
    let stringNum = num.toString();
    let numArray = stringNum.split('');
    let sum = numArray.reduce((acc, curr) => parseInt(acc) + parseInt(curr), 0);
    let length = numArray.length;

    while (sum / length <= 5) {
        numArray.push('9')
        sum += 9;
        length += 1;
    }

    console.log(numArray.join(''));
}

// numberMofidy(101);
// numberMofidy(5835);

// function numberMofidy(num) {
//     let stringNum = num.toString();
//     let numArray = stringNum.split('');
//     let aveCalculate = function(numArray) {
//        return numArray.reduce((acc, curr) => parseInt(acc) + parseInt(curr), 0) / numArray.length;
//     };

//     let average = aveCalculate(numArray);

//     while (average <= 5) {
//         numArray.push('9')
//         average = aveCalculate(numArray);
//     }

//     console.log(numArray.join(''));
// }

// numberMofidy(101);
// numberMofidy(5835);