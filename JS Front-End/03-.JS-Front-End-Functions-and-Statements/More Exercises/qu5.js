function printDNA(num) {
    let sequence = 'ATCGTTAGGG';
    let copySequence = sequence.slice();

    let counter = 0;
    for (let i = 0; i < num; i++) {
        let pair = copySequence.slice(0, 2);
        copySequence = copySequence.slice(2);
        
        if (copySequence.length === 0) { copySequence = sequence.slice() };
    
        counter += 1;
        switch (counter) {
            case 1:
                console.log(`**${pair}**`);
                break;
            case 2:
                console.log(`*${pair[0]}--${pair[1]}*`);
                break;
            case 3:
                console.log(`${pair[0]}----${pair[1]}`);
                break;
            case 4:
                console.log(`*${pair[0]}--${pair[1]}*`);
                counter = 0;
                break;
        }
    }
}

printDNA(4);
// printDNA(10);