function checkLogin(inputArray) {
    let userName = inputArray[0];
    let correctPassword = userName.split('').reverse().join('');
    let attempts = inputArray.slice(1);
    let counter = 0;

    for (password of attempts) {
        counter += 1;
        if (counter === 4 && password !== correctPassword) {
            return console.log(`User ${userName} blocked!`);
        } else if (password === correctPassword) {
            return console.log(`User ${userName} logged in.`);
        } else {
            console.log('Incorrect password. Try again.');
        }
    }
}

// checkLogin(['Acer','login','go','let me in','recA']);
// checkLogin(['momo','omom']);
// checkLogin(['sunny','rainy','cloudy','sunny','not sunny']);
