function toUpperCase(stringInput) {
    let myArray = [];
    let word = '';

    
    for (let char of stringInput) {
        if (/[a-zA-Z0-9]/.test(char)) {
            word += char.toUpperCase();
        } else if (word !== '') {
            myArray.push(word);
            word = '';
        } else {
            continue;
        }
    }

    if (word !== '') {
        myArray.push(word);
    }

    console.log(myArray.join(', '))
}

// toUpperCase('Hi, how are you?')
// toUpperCase('Hello')
toUpperCase('Functions in JS can be nested, i.e. hold other functions')
toUpperCase('0')

