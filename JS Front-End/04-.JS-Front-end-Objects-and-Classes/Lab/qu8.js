function createCats(catsInfo) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

         meow() {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    let cats = [];

    for (let info of catsInfo) {
        let [name, age] = info.split(' ');
        cats.push(new Cat(name, age));
    }

    cats.forEach((cat) => cat.meow());
}

// createCats(['Mellow 2', 'Tom 5']);
// createCats(['Candy 1', 'Poppy 3', 'Nyx 2']);
