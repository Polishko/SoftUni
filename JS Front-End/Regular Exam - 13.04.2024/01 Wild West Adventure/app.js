function solve(input) {
    const num = Number(input.shift());
    const heroList = input.slice(0, num);
    const commandList = input.slice(num);

    const heroes = heroList.reduce((acc, curr) => {
        const [name, hpStr, bulletsStr] = curr.split(' ');
        acc[name] = {
            hp: Number(hpStr),
            bullets: Number(bulletsStr),
        };
        return acc;
    }, {});
    // console.log(heroes);

    for (const item of commandList) {
        const [command, ...rest] = item.split(' - ');
        if (item === 'Ride Off Into Sunset') {
            for (const hero in heroes) {
                console.log(hero);
                console.log(` HP: ${heroes[hero].hp}`);
                console.log(` Bullets: ${heroes[hero].bullets}`);
            }
            break;
        } else if (command === 'FireShot') {
            const [charName, target] = rest;
            if (heroes[charName].bullets > 0) {
                heroes[charName].bullets -= 1;
                console.log(`${charName} has successfully hit ${target} and now has ${heroes[charName].bullets} bullets!`);
            } else {
                console.log(`${charName} doesn't have enough bullets to shoot at ${target}!`);
            }
        } else if (command === 'TakeHit') {
            const [charName, damageStr, attacker] = rest;
            const damage = Number(damageStr);
            heroes[charName].hp -= damage;
            if (heroes[charName].hp > 0) {
                console.log(`${charName} took a hit for ${damage} HP from ${attacker} and now has ${heroes[charName].hp} HP!`);
            } else {
                console.log(`${charName} was gunned down by ${attacker}!`);
                delete heroes[charName];
            }
        } else if (command === 'Reload') {
            const charName = rest[0];
            const oldBullets = heroes[charName].bullets;
            if (oldBullets < 6) {
                heroes[charName].bullets = Math.min(6, oldBullets * 2);
                console.log(`${charName} reloaded ${heroes[charName].bullets - oldBullets} bullets!`);
            } else {
                console.log(`${charName}'s pistol is fully loaded!`);
            }
        } else if (command === 'PatchUp') {
            const [charName, amountStr] = rest;
            const amount = Number(amountStr)
            const oldHp = heroes[charName].hp;
            if (oldHp < 100) {
                heroes[charName].hp = Math.min(100, oldHp + amount);
                console.log(`${charName} patched up and recovered ${heroes[charName].hp - oldHp} HP!`);
            } else {
                console.log(`${charName} is in full health!`);
            }
        }
    }
}

// solve((["2",
//     "Gus 100 0",
//     "Walt 100 6",
//     "FireShot - Gus - Bandit",
//     "TakeHit - Gus - 100 - Bandit",
//     "Reload - Walt",
//     "Ride Off Into Sunset"])
// );

// solve((["2",
//     "Jesse 100 4",
//     "Walt 100 5",
//     "FireShot - Jesse - Bandit",
//     "TakeHit - Walt - 30 - Bandit",
//     "PatchUp - Walt - 20" ,
//     "Reload - Jesse",
//     "Ride Off Into Sunset"])
// );

// solve((["2",
//     "Gus 100 4",
//     "Walt 100 5",
//     "FireShot - Gus - Bandit",
//     "TakeHit - Walt - 100 - Bandit",
//     "Reload - Gus",
//     "Ride Off Into Sunset"])
// );