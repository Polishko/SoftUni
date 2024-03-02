function signCheck(num1, num2, num3) {
    let allNums = [num1, num2, num3];
    let negativeCount = allNums.filter(element => element < 0).length;
    if (negativeCount === 1 | negativeCount === 3) {
        console.log('Negative');
    } else {
        console.log('Positive');
    }
}

// signCheck( 5, 12, -15);
// signCheck( -6, -12, 14);
// signCheck( -1, -2, -3);