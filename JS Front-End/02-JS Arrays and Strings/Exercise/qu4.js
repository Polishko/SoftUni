function sortMinMax(inputArray) {
    let myArray = inputArray.sort((a, b) => a - b);
    let finalArray = [];

    while (myArray.length > 0) {
        let firstNum = myArray.shift();
        let lastNum = myArray.pop();

        finalArray.push(firstNum);

        if (lastNum) {
            finalArray.push(lastNum);
        }
    }

    return finalArray;
}

// console.log(sortMinMax([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));

