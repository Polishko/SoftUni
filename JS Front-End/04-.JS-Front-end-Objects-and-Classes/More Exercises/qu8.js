function getCarInfo(inputArray) {
    const carLog = new Map();

    for (let text of inputArray) {
        let [garageRawInfo, carInfo] = text.split(' - ');
        const garageNo = parseInt(garageRawInfo);

        if (!carLog.has(garageNo)) {
            carLog.set(garageNo, []);
        }

        while (carInfo.includes(': ')) {
            carInfo = carInfo.replace(': ', ' - ');
        }

        const pushText = `--- ${carInfo}`;
        carLog.get(garageNo).push(pushText);
    }

    const sortedCarInfo = Array.from(carLog).sort((a, b) => a[0] - b[0]);

    for (let [no, allCars] of sortedCarInfo) {
        console.log(`Garage № ${no}`);
        allCars.forEach((car) => console.log(car));        
    }
}



// getCarInfo(['1 - color: blue, fuel type: diesel', '1 - color: red, manufacture: Audi', '2 - fuel type: petrol', '4 - color: dark blue, fuel type: diesel, manufacture: Fiat']);
// getCarInfo(['1 - color: green, fuel type: petrol',
// '1 - color: dark red, manufacture: WV',
// '2 - fuel type: diesel',
// '3 - color: dark blue, fuel type: petrol']
// );
