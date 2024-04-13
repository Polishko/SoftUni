function solve(input) {
    const productList = input.shift().split('!');

    for (const action of input) {
        const [command, ...rest] = action.split(' ');
        if (action === 'Go Shopping!') {
            console.log(productList.join(', '));
            break;
        } else if (command === 'Urgent') {
            const item = rest[0];
            if (!productList.includes(item)) {
                productList.unshift(item);
                // productList.splice(0, 0, item);
            }
        } else if (command === 'Unnecessary') {
            const item = rest[0];
            if (productList.includes(item)) {
                const itemIdx = productList.indexOf(item)
                productList.splice(itemIdx, 1);
            }
        } else if (command === 'Correct') {
            const [oldItem, newItem] = rest;
            if (productList.includes(oldItem)) {
                const itemIdx = productList.indexOf(oldItem);
                productList[itemIdx] = newItem;
            }
        } else if (command === 'Rearrange') {
            const item = rest[0];
            if (productList.includes(item)) {
                const itemIdx = productList.indexOf(item)
                productList.splice(itemIdx, 1);
                productList.push(item);
            }
        }
    }
}

// solve((["Tomatoes!Potatoes!Bread",
//     "Unnecessary Milk",
//     "Urgent Tomatoes",
//     "Go Shopping!"])
// );

// solve((["Milk!Pepper!Salt!Water!Banana",
//     "Urgent Salt",
//     "Unnecessary Grapes",
//     "Correct Pepper Onion",
//     "Rearrange Grapes",
//     "Correct Tomatoes Potatoes",
//     "Go Shopping!"])
// );

solve((["Milk!Pepper!Salt!Water!Banana",
    "Urgent Salt",
    "Urgent Pineapple", // Pineapple Milk!Pepper!Salt!Water!Banana
    "Unnecessary Grapes",
    "Unnecessary Milk", //Pineapple !Pepper!Salt!Water!Banana
    "Correct Pepper Onion", // Pineapple !Onion!Salt!Water!Banana
    "Rearrange Onion", // Pineapple !Salt!Water!Banana Onion
    "Correct Tomatoes Potatoes",
    "Go Shopping!"])
);