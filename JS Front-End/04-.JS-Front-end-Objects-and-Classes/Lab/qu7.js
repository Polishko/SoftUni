function sortAddressBook(inputArray) {
    let addressBook = {};

    for (let info of inputArray) {
        let [personName, address] = info.split(':');
        addressBook[personName] = address;
    }

    let sortedEntries = Object.entries(addressBook).sort((a, b) => a[0].localeCompare(b[0]));

    sortedEntries.forEach((entry) => console.log(`${entry[0]} -> ${entry[1]}`));
}

// sortAddressBook(['Tim:Doe Crossing',
// 'Bill:Nelson Place',
// 'Peter:Carlyle Ave',
// 'Bill:Ornery Rd']
// );

// sortAddressBook(['Bob:Huxley Rd',
// 'John:Milwaukee Crossing',
// 'Peter:Fordem Ave',
// 'Bob:Redwing Ave',
// 'George:Mesta Crossing',
// 'Ted:Gateway Way',
// 'Bill:Gateway Way',
// 'John:Grover Rd',
// 'Peter:Huxley Rd',
// 'Jeff:Gateway Way',
// 'Jeff:Huxley Rd']
// );
