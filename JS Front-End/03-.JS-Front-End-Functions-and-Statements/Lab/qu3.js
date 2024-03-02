function repeatStrig(str, num) {
    let result = '';

    for (i = 0; i < num; i++) {
        result += str;
    }

    return result;
}

// console.log(repeatStrig('abc', 3));
// console.log(repeatStrig('String', 2));