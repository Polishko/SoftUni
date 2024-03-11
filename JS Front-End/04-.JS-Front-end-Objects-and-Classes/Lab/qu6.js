function scheduleMeetings(inputArray) {
    let schedule = {};

    for (let info of inputArray) {
        let [day, person] = info.split(' ');

        if (schedule.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`);
        } else {
            console.log(`Scheduled for ${day}`);
            schedule[day] = person;
        }
    }

    Object.entries(schedule).forEach((entry) => console.log(`${entry[0]} -> ${entry[1]}`));
}


// function scheduleMeetings(inputArray) {
//     let schedule = {};

//     for (let info of inputArray) {
//         let [day, person] = info.split(' ');

//         if (day in schedule) {
//             console.log(`Conflict on ${day}!`);
//         } else {
//             console.log(`Scheduled for ${day}`);
//             schedule[day] = person;
//         }
//     }

//     Object.entries(schedule).forEach((entry) => console.log(`${entry[0]} -> ${entry[1]}`));
// }

// scheduleMeetings(['Monday Peter',
// 'Wednesday Bill',
// 'Monday Tim',
// 'Friday Tim']
// );

// scheduleMeetings(['Friday Bob',
// 'Saturday Ted',
// 'Monday Bill',
// 'Monday John',
// 'Wednesday George']
// );