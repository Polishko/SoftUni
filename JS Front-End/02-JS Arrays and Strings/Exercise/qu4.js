function sortMinMax(myArray) {
    myArray.sort((a, b) => a - b);
    finalArray = [];

    while (myArray.length > 0) {
        finalArray.push(myArray.shift());
        finalArray.push(myArray.pop());
    }

    return finalArray;
}

// console.log(sortMinMax([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));

