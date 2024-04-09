function solve(arrayInput) {
    const [horseInfo, ...commands] = arrayInput;
    let horses = horseInfo.split('|');

    let position;
    let newPosition;
    for (const commandInfo of commands) {
        const [command, ...rest] = commandInfo.split(' ');

        if (command === 'Finish') {
            break;
        } else if (command === 'Retake') {
            let [overtaking, overtaken] = rest;
            const idx1 = horses.indexOf(overtaking);
            const idx2 = horses.indexOf(overtaken)
            if (idx1 < idx2) {
                [horses[idx1], horses[idx2]] = [horses[idx2], horses[idx1]]
                console.log(`${overtaking} retakes ${overtaken}.`);
            }
        } else if (command === 'Trouble') {
            const troubledHorse = rest[0];
            if (horses.includes(troubledHorse)) {
                position = horses.indexOf(troubledHorse);
                if (position !== 0) {
                    horses.splice(position, 1);
                    horses.splice(position - 1, 0, troubledHorse);
                    console.log(`Trouble for ${troubledHorse} - drops one position.`);
                }
            }
        } else if (command === 'Rage') {
            const ragedHorse = rest[0];
            position = horses.indexOf(ragedHorse);
            if (horses.includes(ragedHorse)) {
                newPosition = Math.min(position + 2, horses.length - 1);
                horses.splice(position, 1);
                horses.splice(newPosition, 0, ragedHorse);
                console.log(`${ragedHorse} rages 2 positions ahead.`);
            }
        } else if (command === 'Miracle') {
            const lastHorse = horses.shift();
            horses.push(lastHorse);
            console.log(`What a miracle - ${lastHorse} becomes first.`);
        }
    }
    console.log(horses.join('->'));
    let winner = horses.pop();
    if (winner) {
        console.log(`The winner is: ${winner}`);
    }
}
