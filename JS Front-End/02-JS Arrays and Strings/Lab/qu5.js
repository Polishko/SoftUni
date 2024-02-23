function replaceWord(text, word) {
    while (text.includes(word)) {
        let replacement = '*'.repeat(word.length);
        text = text.replace(word, replacement);
    }

    console.log(text);
}


// replaceWord('A small sentence with some words', 'small');
// replaceWord('Find the hidden word', 'hidden');
