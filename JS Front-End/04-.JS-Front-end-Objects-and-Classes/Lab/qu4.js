function objectToString(firstName, lastName, hairColor) {
    let person = {};
    person.name = firstName;
    person.lastName = lastName;
    person.hairColor = hairColor;
    let text = JSON.stringify(person);
    console.log(text);
}


// objectToString('George', 'Jones', 'Brown');
// objectToString('Peter', 'Smith', 'Blond');