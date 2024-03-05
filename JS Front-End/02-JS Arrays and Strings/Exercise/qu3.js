function sortAndPrint(myArray) {
    let lowerCaseArray = myArray
                            .sort((a, b) => a.localeCompare(b))
                            .forEach((personName, idx) => console.log(`${idx + 1}.${personName}`));
    }


// function sortAndPrint(myArray) {
//     let lowerCaseArray = myArray.map(personName => personName.toLowerCase()).sort();
//     let counter = 0;

//     for (loweredName of lowerCaseArray) {

//         while (myArray.length > 0) {
//             let current = myArray.shift();
//             if (current.toLowerCase() === loweredName) {
//                 counter += 1;
//                 console.log(`${counter}.${current}`);
//                 break;
//             }
//             myArray.push(current);
//             }
//         }
//     }

// sortAndPrint(["John", "Bob", "Christina", "Ema"]);
// sortAndPrint(["Bob", "abe", "Christina", "Ema"]);
