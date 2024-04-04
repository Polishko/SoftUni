function solve(input) {
    const [n, info] = [Number(input[0]), input.slice(1)];
    const [people, commands] = [info.slice(0, n), info.slice(n)];

    const team = people.reduce((acc, curr) => {
        let [name, capacity, position] = curr.split('|');
        acc[name] = {'capacity': Number(capacity), 'position': Number(position)};
        return acc;
    }, {});

    for (const commandInfo of commands) {
        let [command, ...rest] = commandInfo.split(' - ');

        switch (command) {
            case 'StopForFuel':
                let [name, minFuel, changed] = rest;
                if (team[name].capacity < Number(minFuel)) {
                    team[name].position = changed;
                    console.log(`${name} stopped to refuel but lost his position, now he is ${changed}.`);
                } else {
                    console.log(`${name} does not need to stop for fuel!`);
                }
                break;
            case 'Overtaking':
                let [first, second] = rest;
                let [firstPos, secondPos] = [team[first].position, team[second].position];
                if (firstPos < secondPos) {
                    team[first].position = secondPos;
                    team[second].position = firstPos;
                    console.log(`${first} overtook ${second}!`)
                }
                break;
            case 'EngineFail':
                let [rider, lapsLeft] = rest;
                delete team[rider];
                console.log(`${rider} is out of the race because of a technical issue, ${lapsLeft} laps before the finish.`)
                break;
            case 'Finish':
                for (let member in team) {
                    console.log(member);
                    console.log(`  Final position: ${team[member].position}`)
                }
                break;
        }
    }
}

// solve((["3",
//     "Valentino Rossi|100|1",
//     "Marc Marquez|90|2",
//     "Jorge Lorenzo|80|3",
//     "StopForFuel - Valentino Rossi - 50 - 1",
//     "Overtaking - Marc Marquez - Jorge Lorenzo",
//     "EngineFail - Marc Marquez - 10",
//     "Finish"])
// );

// solve(["4",
//     "Valentino Rossi|100|1",
//     "Marc Marquez|90|3",
//     "Jorge Lorenzo|80|4",
//     "Johann Zarco|80|2",
//     "StopForFuel - Johann Zarco - 90 - 5",
//     "Overtaking - Marc Marquez - Jorge Lorenzo",
//     "EngineFail - Marc Marquez - 10",
//     "Finish"]
// );
