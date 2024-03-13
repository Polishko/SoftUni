// lecture note: can be also solved with Set()
// No need for so many checks because no such edge cases in Judge
// Just set this while iterating carsInLot[carPlate] = (direction === 'IN') so its either true or false and then you filter only true ones

function getCarRecords(inputArray) {
    let carsInLot = {};
    for (let info of inputArray) {
        const [direction, carPlate] = info.split(', ');

        if ((direction === 'IN')
         || (carsInLot.hasOwnProperty(carPlate) && carsInLot[carPlate] === 'IN' && direction === 'OUT')) {
            carsInLot[carPlate] = direction;
        }
    }

    let allCars = [];
    Object.entries(carsInLot).forEach((entry) => {
        if (entry[1] === 'IN') {
            allCars.push(entry[0]);
        }
    })
    
    allCars = allCars.sort((a, b) => a.localeCompare(b));

    allCars.length > 0 ? allCars.forEach((number) => console.log(number)) : console.log('Parking Lot is Empty');   
}

// function getCarRecords(inputArray) {
//     let carsInLot = new Map();
//     for (let info of inputArray) {
//         const [direction, carPlate] = info.split(', ');

//         let number = carsInLot.get(carPlate) || 0;
//         if (direction == 'IN' && number === 0) {
//             carsInLot.set(carPlate, direction);
//         } else if ((direction == 'OUT' && number !== 0)) {
//             carsInLot.delete(carPlate);
//         }
//     }

//     const sortedCars = [...carsInLot.keys()].sort((a, b) => a.localeCompare(b));

//     sortedCars.length > 0 ? sortedCars.forEach((number) => console.log(number)) : console.log('Parking Lot is Empty');
// }

getCarRecords(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
);

// getCarRecords(['IN, CA2844AA',
// 'IN, CA1234TA',
// 'OUT, CA2844AA',
// 'OUT, CA1234TA']
// );
