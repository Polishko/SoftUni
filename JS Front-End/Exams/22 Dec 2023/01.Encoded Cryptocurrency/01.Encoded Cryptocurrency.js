function decryptMessage(inputArray) {
    let [message, ...commands] = inputArray;
    let subString;
    let replacement;

    for (const command of commands) {
        const commandWords = command.split('?')
        switch (commandWords[0]) {
            case 'TakeEven':
                message = Array.from(message).filter((char, idx) => idx % 2 === 0).join('');
                console.log(message);
                break;
            case 'ChangeAll':
                [subString, replacement] = [commandWords[1], commandWords[2]];
                while (message.includes(subString)) {
                    message = message.replace(subString, replacement);
                }
                console.log(message);
                break;
            case 'Reverse':
                subString = commandWords[1];
                if (message.includes(subString)) {
                    message = message.replace(subString, '');
                    message += subString.split('').reverse().join('');
                    console.log(message);
                } else {
                    console.log('error');
                }
                break;
            case 'Buy':
                console.log(`The cryptocurrency is: ${message}`);
        }
    }
}


// decryptMessage((["z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs", 
// "TakeEven",
// "Reverse?!nzahc",
// "ChangeAll?m?g",
// "Reverse?adshk",
// "ChangeAll?z?i",
// "Buy"])
// );

decryptMessage((["PZDfA2PkAsakhnefZ7aZ", 
"TakeEven",
"TakeEven",
"TakeEven",
"ChangeAll?Z?X",
"ChangeAll?A?R",
"Reverse?PRX",
"Buy"])
);