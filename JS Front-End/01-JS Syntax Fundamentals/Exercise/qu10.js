function isSame(num) {
    let current;
    let next;
    let sumNums = 0;
    let result = 'true'

    while (num > 0) {
        current = num % 10;
        num = Math.floor(num / 10)
        next = num % 10;
        sumNums += current;

        if (num !== 0 && result === 'true' && next !== current) {
            result = 'false'
        }
    }

    console.log(`${result}\n${sumNums}`)
}


isSame(2222222)
isSame(1234)
