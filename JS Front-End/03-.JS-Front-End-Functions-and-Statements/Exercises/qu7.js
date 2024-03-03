function nXNMatrix(num) {
    for (i = 0; i < num; i++) {
        numArray = Array.from({length: num}, () => num);
        console.log(numArray.join(' '));
    }
}

// nXNMatrix(3);
// nXNMatrix(7);
// nXNMatrix(2);