// needs correction
function solve(arrayInput) {
    const [horseInfo, ...commands] = arrayInput;
    let horses = horseInfo.split('|');

    let position;
    let newPosition;
    for  (const commandInfo of commands) {
        const [command, ...rest] = commandInfo.split(' ');

        switch (command) {
            case 'Retake':
                let [overtaking, overtaken] = rest;
                const idx1 = horses.indexOf(overtaking);
                const idx2 = horses.indexOf(overtaken)
                if (idx1 < idx2) {
                    horses[idx1] = overtaken;
                    horses[idx2] = overtaking;
                    console.log(`${overtaking} retakes ${overtaken}.`);
                }
                break;
            case 'Trouble':
                const troubledHorse = rest[0];
                position = horses.indexOf(troubledHorse);
                if (position !== 0) {
                    horses.splice(position, 1);
                    horses.splice(position - 1, 0, troubledHorse);
                    console.log(`Trouble for ${troubledHorse} - drops one position.`);
                }
                break;
            case 'Rage':
                const ragedHorse = rest[0];
                position = horses.indexOf(ragedHorse);
                if (position !== horses.length - 1) {
                    newPosition= Math.min(position + 2, horses.length - 1);
                    horses.splice(position, 1);
                    horses.splice(newPosition, 0, ragedHorse);
                    console.log(`${ragedHorse} rages 2 positions ahead.`);
                }
                break;
            case 'Miracle':
                const lastHorse = horses.shift();
                horses.push(lastHorse);
                console.log(`What a miracle - ${lastHorse} becomes first.`);
                break;
            case 'Finish':
                console.log(horses.join('->'));
                let winner = horses.pop();
                if (winner) {
                    console.log(`The winner is: ${winner}`);
                }
                return;
        }
    }
}

// solve((['Bella|Alexia|Sugar',
//     'Retake Alexia Sugar',
//     'Rage Bella',
//     'Trouble Bella',
//     'Finish'])
// );

// solve((['Onyx|Domino|Sugar|Fiona',
//     'Trouble Onyx',
//     'Retake Onyx Sugar',
//     'Rage Domino',
//     'Miracle',
//     'Finish'])
// );

// solve((['Fancy|Lilly',
//     'Retake Lilly Fancy',
//     'Trouble Lilly',
//     'Trouble Lilly',
//     'Finish',
//     'Rage Lilly'])
// );

solve((['',
    'Finish',
    ])
);
