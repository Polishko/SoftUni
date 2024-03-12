function getFlightInfo(mainArray) {
    const [array1, array2, array3] = [mainArray[0], mainArray[1], mainArray[2]];
    let allFlights = {};
    let status = 'Ready to fly';

    for (let info1 of array1) {
        let [number, destination] = info1.split(' ');
        allFlights[number] = {
            Destination: destination,
            Status: status,
        };
    }

    for (info2 of array2) {
        let number = info2.split(' ')[0];
        if (allFlights.hasOwnProperty(number)) {
            allFlights[number].Status = 'Cancelled';
        }
    }

    let filteredFlights = Object.entries(allFlights).filter((entry) => entry[1].Status === array3[0]);

   filteredFlights.forEach((entry) => console.log(`{ Destination: '${entry[1].Destination}', Status: '${entry[1].Status}' }`));
}


// getFlightInfo([['WN269 Delaware',
// 'FL2269 Oregon',
//  'WN498 Las Vegas',
//  'WN3145 Ohio',
//  'WN612 Alabama',
//  'WN4010 New York',
//  'WN1173 California',
//  'DL2120 Texas',
//  'KL5744 Illinois',
//  'WN678 Pennsylvania'],
//  ['DL2120 Cancelled',
//  'WN612 Cancelled',
//  'WN1173 Cancelled',
//  'SK430 Cancelled'],
//  ['Cancelled']
// ]
// );

getFlightInfo([['WN269 Delaware',
'FL2269 Oregon',
 'WN498 Las Vegas',
 'WN3145 Ohio',
 'WN612 Alabama',
 'WN4010 New York',
 'WN1173 California',
 'DL2120 Texas',
 'KL5744 Illinois',
 'WN678 Pennsylvania'],
 ['DL2120 Cancelled',
 'WN612 Cancelled',
 'WN1173 Cancelled',
 'SK330 Cancelled'],
 ['Ready to fly']
]
);
