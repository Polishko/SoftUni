function printCityInfo(city) {
    Object.entries(city).forEach((entry) => console.log(`${entry[0]} -> ${entry[1]}`));
}


printCityInfo({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000"
}
);
