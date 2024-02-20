function findSum (num1, num2) {
    let allNums = [];
    let sumNums = 0;

    for (let i=num1; i<=num2; i++) {
        allNums.push(i);
        sumNums += i;
    }

    console.log(`${allNums.join(' ')}\nSum: ${sumNums}`);
}

findSum(5, 10);
findSum(0, 26);
findSum(50, 60);


// function findSum (num1, num2) {
//     let allNums = '';
//     let sumNums = 0;
//     let current;

//     for (let i=num1; i<=num2; i++) {
//         current = i;
//         allNums = allNums + current + ' ';
//         sumNums += i;
//     }

//     console.log(`${allNums.trim()}\nSum: ${sumNums}`);
// }

