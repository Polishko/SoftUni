function validatePassword(myString) {
    let validateLength = function (myString) {
        let stringLength = myString.length;

        if (stringLength < 6 || stringLength > 10) {
            console.log(`Password must be between 6 and 10 characters`);
            return false;
        }

        return true;
    };

    let validateType = function (myString) {
        let result = /^[A-Za-z0-9]+$/.test(myString);

        if (result === false) {
            console.log(`Password must consist only of letters and digits`);
        }

        return result;
    };

    let validatDigitCount = function (myString) {
        let matches = myString.match(/(\d+)/g);
        if (!matches || matches[0].length < 2) {
            console.log(`Password must have at least 2 digits`);
            return false;
        }

        return true;
    };

    let isLengthValid = validateLength(myString);
    let isTypeValid = validateType(myString);
    let isDigitCountValid = validatDigitCount(myString);

    if (isLengthValid && isTypeValid && isDigitCountValid) {
        console.log(`Password is valid`);
    }
}

// validatePassword('logIn');
// validatePassword('MyPass123');
// validatePassword('Pa$s$s');