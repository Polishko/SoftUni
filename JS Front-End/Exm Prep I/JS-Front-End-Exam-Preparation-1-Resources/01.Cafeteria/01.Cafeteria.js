function main(input) {
    const numBaristas = Number(input[0]);
    const teamInfo = input.slice(1, numBaristas + 1);
    const commands = input.slice(numBaristas + 1);
    const team = teamInfo.reduce((acc, curr) => {
        const [name, shift, allSkills] = curr.split(' ');
        acc[name] = { 'shift': shift, 'skills': allSkills.split(',') }
        return acc 
    }, {});

    let baristaName;
    let shift;
    let drink;
    let baristaDrinks;
    let baristaShift;

    for (const commandElement of commands) {
        const command = commandElement.split(' / ');
        const [mainCommand, commandInfo] = [command[0], command.slice(1)]

        switch (mainCommand){
            case 'Prepare':
                [baristaName, shift, drink] = commandInfo;
                [baristaShift, baristaDrinks] = [team[baristaName].shift, team[baristaName].skills];
                if (shift === baristaShift && baristaDrinks.includes(drink)) {
                    console.log(`${baristaName} has prepared a ${drink} for you!`);
                } else {
                    console.log(`${baristaName} is not available to prepare a ${drink}.`);
                }
                break;
            case 'Change Shift':
                [baristaName, shift] = commandInfo;
                team[baristaName].shift = shift;
                console.log(`${baristaName} has updated his shift to: ${shift}`); //If not changed edge case?
                break;
            case 'Learn':
                [baristaName, drink] = commandInfo;

                if (team[baristaName].skills.includes(drink)) {
                    console.log(`${baristaName} knows how to make ${drink}.`);
                } else {
                    team[baristaName].skills.push(drink);
                    console.log(`${baristaName} has learned a new coffee type: ${drink}.`);
                }
                break;
            case 'Close':
                break;
        }
    }

    // Barista info
    for (const barista in team) {
        console.log(`Barista: ${barista}, Shift: ${team[barista].shift}, Drinks: ${team[barista].skills.join(', ')}`);
    }
}

// main([
//     '3',
//       'Alice day Espresso,Cappuccino',
//       'Bob night Latte,Mocha',
//       'Carol day Americano,Mocha',
//       'Prepare / Alice / day / Espresso',
//       'Change Shift / Bob / night',
//       'Learn / Carol / Latte',
//       'Learn / Bob / Latte',
//       'Prepare / Bob / night / Latte',
//       'Closed']
// )

// main(['4',
// 'Alice day Espresso,Cappuccino',
// 'Bob night Latte,Mocha',
// 'Carol day Americano,Mocha',
// 'David night Espresso',
// 'Prepare / Alice / day / Espresso',
// 'Change Shift / Bob / day',
// 'Learn / Carol / Latte',
// 'Prepare / Bob / night / Latte',
// 'Learn / David / Cappuccino',
// 'Prepare / Carol / day / Cappuccino',
// 'Change Shift / Alice / night',
//  'Learn / Bob / Mocha',
// 'Prepare / David / night / Espresso',
// 'Closed']
// )