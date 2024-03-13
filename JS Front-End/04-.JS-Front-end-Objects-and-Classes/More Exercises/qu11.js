function getShelvesLog(inputArray) {
    const shelves = new Map();

    for (info of inputArray) {
        if (info.includes('->')) {
            let [id, genre] = info.split(' -> ');
            
            let shelfExists = false;
            for (key of shelves.keys()) {
                if (key[0] === parseInt(id)) {
                    shelfExists = true;
                    break;
                }
            }
            
            if (!shelfExists) {
                shelves.set([parseInt(id), genre], []);
            }

        } else if (info.includes(':')) {
            let [part1, part2] = info.split(': ');
            let title = part1;
            let [author, genre] = part2.split(', ');

            for (key of shelves.keys()) {
                if (key[1] === genre) {
                    shelves.get(key).push([title, author]);
                }
            }
        }
    }

    const sortedShelves = Array.from(shelves).sort((a, b) => {
        const lenA = a[1].length;
        const lenB = b[1].length;
        return lenB - lenA;
    });

        for (let shelve of sortedShelves) {
            let no = shelve[0][0];
            let genre = shelve[0][1]
            let books = shelve[1].sort((a, b) => a[0].localeCompare(b[0]));
            console.log(`${no} ${genre}: ${books.length}`);
            books.forEach((book) => console.log(`--> ${book[0]}: ${book[1]}`));
        }   
}

// getShelvesLog(['1 -> history', '1 -> action', 'Death in Time: Criss Bell, mystery',
//  '2 -> mystery', '3 -> sci-fi', 'Child of Silver: Bruce Rich, mystery',
//   'Hurting Secrets: Dustin Bolt, action', 'Future of Dawn: Aiden Rose, sci-fi',
//    'Lions and Rats: Gabe Roads, history', '2 -> romance', 'Effect of the Void: Shay B, romance',
//     'Losing Dreams: Gail Starr, sci-fi', 'Name of Earth: Jo Bell, sci-fi', 'Pilots of Stone: Brook Jay, history']);

// getShelvesLog(['1 -> mystery', '2 -> sci-fi',
// 'Child of Silver: Bruce Rich, mystery',
// 'Lions and Rats: Gabe Roads, history',
// 'Effect of the Void: Shay B, romance',
// 'Losing Dreams: Gail Starr, sci-fi',
// 'Name of Earth: Jo Bell, sci-fi']
// );