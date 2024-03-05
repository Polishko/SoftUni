// A much better alternative that can catch exact matches while the one below has extra regex to avoid catching substrings
function splitter(myString) {
    const regexp = /[A-Z][a-z]*/g;
    const allMatches = myString.matchAll(regexp);
    const words = Array.from(allMatches).map(match => match[0]);
    
    console.log(words.join(', '));
}

// function splitter(myString) {
//     let regexp = /[A-Z][a-z\d]*(?=[A-Z]|$)/g;
//     // let regexp = /[A-Z][a-z\d]*/g; wont correctly catch last example
//     let allMatches = myString.match(regexp);

//     if (allMatches) {
//         console.log(allMatches.join(', '));
//     }
// }

// splitter('SplitMeIfYouCanHaHaYouCantOrYouCan');
// splitter('HoldTheDoor');
// splitter('ThisIsSoAnnoyingToDo');
// splitter('OpenApi3Specification**A3');
