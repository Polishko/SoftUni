function createPhoneBook(infoArray) {
    let phoneBook = {};

    for (let info of infoArray) {
        let [firstName, phoneNumber] = info.split(' ');
        phoneBook[firstName] = phoneNumber;    
    }

    for (let key in phoneBook) {
        console.log(`${key} -> ${phoneBook[key]}`);
    }
    
}

// createPhoneBook(['Tim 0834212554',
// 'Peter 0877547887',
// 'Bill 0896543112',
// 'Tim 0876566344']
// );

// createPhoneBook(['George 0552554',
// 'Peter 087587',
// 'George 0453112',
// 'Bill 0845344']
// );