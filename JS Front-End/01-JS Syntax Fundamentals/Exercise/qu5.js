function numberTable(num) {
    let numTable = [];

    for (let i=1; i<=10; i++) {
        numTable.push(`${num} X ${i} = ${num * i}`);
    }

    console.log(numTable.join('\n'));
}


// numberTable(2);