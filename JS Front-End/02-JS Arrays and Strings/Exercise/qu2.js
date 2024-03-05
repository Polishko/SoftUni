function takeSteps(myArray, num) {
    let newArray = myArray.filter((ele, index) => index % num === 0);

    return newArray;
}

// function takeSteps(myArray, num) {
//     let newArray = [];
//     for (i=0; i<myArray.length; i+=num) {
//         newArray.push(myArray[i]);
//     }

//     return newArray;
// }

// console.log(takeSteps(['5', '20', '31', '4', '20'], 2));
// console.log(takeSteps(['dsa','asd', 'test', 'tset'], 2));
// console.log(takeSteps(['1', '2','3', '4', '5'], 6));
