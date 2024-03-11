function listTowns(inputArray) {
    class Town {
        constructor(name, latitude, longitude) {
            this.name = name;
            this.latitude = latitude;
            this.longitude = longitude;
        }

        toString() {
            return `{ town: '${this.name}', latitude: '${this.latitude}', longitude: '${this.longitude}' }`;
        }
    }

    let towns = [];
    for (let info of inputArray) {
        const [townName, townLatitude, townLongitude] = info.split(' | ');
        towns.push(new Town(townName, Number(townLatitude).toFixed(2), Number(townLongitude).toFixed(2)));
    }

    return towns.join('\n');
}

// console.log(listTowns(['Sofia | 42.696552 | 23.32601',
// 'Beijing | 39.913818 | 116.363625']
// ));

// console.log(listTowns(['Plovdiv | 136.45 | 812.575']));