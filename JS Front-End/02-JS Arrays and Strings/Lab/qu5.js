// Replacing all matches using RegExp

function replaceWord(text, word) {
    const pattern = new RegExp(word, 'g');
    const result = text.replace(pattern, '*'.repeat(word.length));

    console.log(result);
}

// Other solutions

// function replaceWord(text, word) {
//     while (text.includes(word)) {
//         let replacement = '*'.repeat(word.length);
//         text = text.replace(word, replacement);
//     }

//     console.log(text);
// }

// function replaceWord(text, word) {
//     let idx = text.indexOf(word);

//     while (idx >= 0) {
//         let replacement = '*'.repeat(word.length);
//         text = text.replace(word, replacement);

//         idx = text.indexOf(word);
//     }

//     console.log(text);
// }

// replaceWord('A small sentence with some words', 'small');
// replaceWord('Find the hidden word', 'hidden');
