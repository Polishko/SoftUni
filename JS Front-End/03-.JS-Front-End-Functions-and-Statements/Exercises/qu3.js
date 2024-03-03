function charactersInRange(char1, char2) {
    let order1 = char1[0].charCodeAt(0);
    let order2 = char2[0].charCodeAt(0);

    if (order2 < order1) {
        sum = order1 + order2;
        order2 = order1;
        order1 = sum - order2;
    }

    let symbolsRange = Array.from(
        {length: order2 - order1 - 1}, (_, index) => (String.fromCharCode(order1 + index + 1))
        );

    console.log(symbolsRange.join(' '));

}

// charactersInRange('a', 'd');
// charactersInRange('#', ':')
// charactersInRange('C', '#')
// charactersInRange('#', 'C')
