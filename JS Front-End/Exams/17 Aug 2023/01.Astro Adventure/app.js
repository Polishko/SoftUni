function solve(input) {
    const [n, ...info] = input;
    const num = Number(n);
    const peopleInfo = info.slice(0, num);
    const commands = info.slice(num);

    let team = peopleInfo.reduce((acc, curr) => {
        const [name, oxygen, energy] = curr.split(' ');
        acc[name] = {'oxygen': Number(oxygen), 'energy': Number(energy)};
        return acc;
    }, {});

    for (const commandElement of commands) {
        let [command, astronaut, amountString] = commandElement.split(' - ');
        const amount = Number(amountString);
        switch (command) {
            case 'Explore':
                if (team[astronaut].energy >= (amount)) {
                    team[astronaut].energy -= amount;
                    console.log(`${astronaut} has successfully explored a new area and now has ${team[astronaut].energy} energy!`);
                } else {
                    console.log(`${astronaut} does not have enough energy to explore!`);
                }
                break;
            case 'Refuel':
                const oldEnergy = team[astronaut].energy;
                team[astronaut].energy = Math.min(oldEnergy + amount, 200);
                console.log(`${astronaut} refueled their energy by ${team[astronaut].energy - oldEnergy}!`);
                break;
            case 'Breathe':
                const oldOxygen = team[astronaut].oxygen;
                team[astronaut].oxygen = Math.min(oldOxygen + amount, 100);
                console.log(`${astronaut} took a breath and recovered ${team[astronaut].oxygen - oldOxygen} oxygen!`);
                break;
            case 'End':
                for (const person in team) {
                    console.log(`Astronaut: ${person}, Oxygen: ${team[person].oxygen}, Energy: ${team[person].energy}`);
                }
                break;
        }
    }
}



// solve([  '3',
//     'John 50 120',
//     'Kate 80 180',
//     'Rob 70 150',
//     'Explore - John - 50',
//     'Refuel - Kate - 30',
//     'Breathe - Rob - 20',
//     'End']
// );

// solve([    '4',
//     'Alice 60 100',
//     'Bob 40 80',
//     'Charlie 70 150',
//     'Dave 80 180',
//     'Explore - Bob - 60',
//     'Refuel - Alice - 30',
//     'Breathe - Charlie - 50',
//     'Refuel - Dave - 40',
//     'Explore - Bob - 40',
//     'Breathe - Charlie - 30',
//     'Explore - Alice - 40',
//     'End']
// );