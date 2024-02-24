function rotateArray(myArray, num) {
    for (let i = 1; i <= num; i++) {
        myArray.push(myArray.shift());
    }

    console.log(myArray.join(' '));
}

// rotateArray([51, 47, 32, 61, 21], 2);
// rotateArray([32, 21, 61, 1], 4);
// rotateArray([2, 4, 15, 31], 5);