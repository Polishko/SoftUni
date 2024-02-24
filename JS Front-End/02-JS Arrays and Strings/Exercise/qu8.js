function splitter(myString) {
    let regexp = /[A-Z][a-z\d]*(?=[A-Z]|$)/g;
    // let regexp = /[A-Z][a-z\d]*/g; wont correctly catch last example
    let allMatches = myString.match(regexp);

    if (allMatches) {
        console.log(allMatches.join(', '));
    }
}

// splitter('SplitMeIfYouCanHaHaYouCantOrYouCan');
// splitter('HoldTheDoor');
// splitter('ThisIsSoAnnoyingToDo');
// splitter('OpenApi3Specification**A3');
