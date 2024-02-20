
function speedLimit(speed, area) {
    const limits = {
        'motorway': 130,
        'interstate': 90,
        'city': 50,
        'residential': 20,
    } 

    let result;
    let difference = speed - limits[area];


    if (difference <= 0) {
        result = `Driving ${speed} km/h in a ${limits[area]} zone`;
    } else if (difference > 40 ) {
        result = `The speed is ${difference} km/h faster than the allowed speed of ${limits[area]} - reckless driving`;
    } else if (difference > 20 ) {
        result = `The speed is ${difference} km/h faster than the allowed speed of ${limits[area]} - excessive speeding`;
    } else {
        result = `The speed is ${difference} km/h faster than the allowed speed of ${limits[area]} - speeding`;
    }

    console.log(result);
}


// speedLimit(40, 'city');
// speedLimit(21, 'residential');
// speedLimit(120, 'interstate');