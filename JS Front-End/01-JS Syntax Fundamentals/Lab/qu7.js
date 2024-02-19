function solve(dayType, age) {
    const tickets = {
        'Weekday': [12, 18, 12],
        'Weekend': [15, 20, 15],
        'Holiday': [5, 12, 10]
    };

    let result;

    if (age < 0 || age > 122) {
        result = 'Error!';   
    } else if (age <= 18) {
        result = `${tickets[dayType][0]}\$`;
    } else if (age <= 64) {
        result = `${tickets[dayType][1]}\$`;
    } else {
        result = `${tickets[dayType][2]}\$`;
    }

    console.log(result);
}

solve('Holiday', 15);