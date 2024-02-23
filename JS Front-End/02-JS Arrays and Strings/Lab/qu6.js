function replaceWord(text, word) {
    let textArray = text.split(' ');
    let count = textArray.reduce((acc, curr) => (curr === word ? acc + 1 : acc), 0);
    console.log(count);
}

replaceWord('This is a word and it also is a sentence', 'is');
replaceWord('softuni is great place for learning new programming languages', 'softuni');