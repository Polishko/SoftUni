// without class make a list of heroes and add heros as object created dinamically in the for loop
// for every row of input array map it to split it, map again to take deconstructed form and return the object

function createInventory(infoArray) {
    class Hero {
        constructor(name, level, items) {
            this.name = name;
            this.level = level;
            this.items = items;
        }

        toString() {
            return `Hero: ${this.name}\nlevel => ${this.level}\nitems => ${this.items.join(', ')}`;
        }
    }

    let heroList = [];
    for (let log of infoArray) {
        const [heroName, heroLevel, ...heroItems] = log.split(' / ');
        heroList.push(new Hero(heroName, heroLevel, heroItems));
    }

    heroList.sort((a, b) => a.level - b.level);
    return heroList.join('\n');
}


// console.log(createInventory([
//     'Isacc / 25 / Apple, GravityGun',
//     'Derek / 12 / BarrelVest, DestructionSword',
//     'Hes / 1 / Desolator, Sentinel, Antara'
//     ]
//     ));

console.log(createInventory([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
    ])
    );
