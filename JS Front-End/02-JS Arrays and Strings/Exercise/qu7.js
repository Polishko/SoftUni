function hasSubstring(word, myString) {
    myArray = myString.split(' ');

    for (text of myArray) {
        if (text.toLowerCase() === word.toLowerCase()) {
            return console.log(word);
        }
    }

    return console.log(`${word} not found!`)
}


// hasSubstring('javascript', 'JavaScript is the best programming language');
// hasSubstring('python', 'JavaScript is the best programming language');
