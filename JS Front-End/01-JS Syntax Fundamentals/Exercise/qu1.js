function calculate(num) {
    const low_boundary = 0;
    const high_bounary = 65;

    let age_groups = {
        'baby': [0, 2],
        'child': [3, 13],
        'teenager': [14, 19],
        'adult': [20, 65],
    }

    let result;

    if (num < low_boundary) {
        result = 'out of bounds';
    }

    else if (num > high_bounary) {
        result = 'elder';
    }

    else {
        for (let key in age_groups) {
            if (age_groups[key][0] <= num && num <=age_groups[key][1]) {
                result = key;
                break;
            }
           }
    }
   
   console.log(result);
}

// calculate(-1)