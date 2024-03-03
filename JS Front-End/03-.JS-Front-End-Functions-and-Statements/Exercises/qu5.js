function palindromeCheck(myArray) {
    let isPalindrome = function(str) {
        let mid_length = Math.floor(str.length / 2);
    
        for (let i = 0; i < mid_length; i++) {
            if (str[i] !== str[str.length - 1 - i]) {
                return false;
            }
        }
    
        return true
    }

    for (num of myArray) {
        let numString = num.toString();
        if (numString.length === 1) {
            console.log(true);
        } else {
            console.log(isPalindrome(numString));
        }
    }
}

// palindromeCheck([123,323,421,121]);
// palindromeCheck([32,2,232,1010]);

// function palindromeCheck(myArray) {
//     for (num of myArray) {
//         let numString = num.toString();

//         if (numString.length === 1) {
//             console.log('true');
//         } else {
//             let length = (numString.length % 2  !== 0) ? (numString.length - 1) / 2 : numString.length / 2;
//             let result1 = numString.slice(0, length);
//             let result2 = [...numString].reverse().join('').slice(0, length);
//             console.log(result1 === result2);
//         }      
//     }
// }

