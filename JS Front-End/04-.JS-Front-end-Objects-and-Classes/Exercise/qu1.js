# alternative from lecture
function listEmployees(employeeNames) {
    employeeNames.map(name => ({ name, personalNumber: name.length }))
    .forEach((employee) => console.log(`Name: ${employee.name} -- Personal Number: ${employee.personalNumber}`));
}


// function listEmployees(inputArray) {
//     class Employee {
//         constructor(name, number) {
//             this.name = name;
//             this.number = number;
//         }
//     }

//     let employees = [];
//     for (let info of inputArray) {
//         const [emloyeeName, personalNumber] = [info, info.length];
//         employees.push(new Employee(emloyeeName, personalNumber));
//     }

//     employees.forEach((employee) => console.log(`Name: ${employee.name} -- Personal Number: ${employee.number}`));
// }

// listEmployees([
//     'Silas Butler',
//     'Adnaan Buckley',
//     'Juan Peterson',
//     'Brendan Villarreal'
//     ]
//     );

// listEmployees([
//     'Samuel Jackson',
//     'Will Smith',
//     'Bruce Willis',
//     'Tom Holland'
//     ]
//     );
