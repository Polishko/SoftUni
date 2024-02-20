

function chopChop(num, para1, para2, para3, para4, para5) {
    let items = [para1, para2, para3, para4, para5];
    const operations = {
        'chop': () => num / 2,
        'dice': () => Math.sqrt(num),
        'spice': () => num + 1,
        'bake': () => num * 3,
        'fillet': () => num * 0.8
    };

    let operation;

    for (let i = 0; i < items.length; i++) {
        operation = items[i];
        num = operations[operation]();
        console.log(num);
    }
}


// chopChop('32', 'chop', 'chop', 'chop', 'chop', 'chop');
chopChop('9', 'dice', 'spice', 'chop', 'bake', 'fillet');