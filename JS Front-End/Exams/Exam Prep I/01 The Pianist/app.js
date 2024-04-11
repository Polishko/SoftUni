function solve(input) {
    const num = Number(input.shift());
    const pieces = input.slice(0, num).reduce((acc, curr) => {
        const [piece, composer, key] = curr.split('|');
        acc[piece] = { composer, key };
        return acc;
    }, {});

    const commands = input.slice(num);
    for (const item of commands) {
        const [command, ...rest] = item.split('|');

        if (command === 'Stop') {
            printPieces();
            break;
        } else if (command === 'Add') {
            const [piece, composer, key] = rest;
            if (pieces.hasOwnProperty(piece)) {
                console.log(`${piece} is already in the collection!`);
            } else {
                pieces[piece] = { composer, key };
                console.log(`${piece} by ${composer} in ${key} added to the collection!`);
            }
        } else if (command === 'Remove') {
            const piece = rest[0];
            if (!pieces.hasOwnProperty(piece)) {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            } else {
                delete pieces[piece];
                console.log(`Successfully removed ${piece}!`);
            }
        } else if (command === 'ChangeKey') {
            const [piece, newKey] = rest;
            if (!pieces.hasOwnProperty(piece)) {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            } else {
                pieces[piece].key = newKey;
                console.log(`Changed the key of ${piece} to ${newKey}!`);
            }
        }
    }

    function printPieces() {
        Object.keys(pieces).forEach(piece => {
            console.log(`${piece} -> Composer: ${pieces[piece].composer}, Key: ${pieces[piece].key}`);
        })
    }
}

// solve([
//         '3',
//         'Fur Elise|Beethoven|A Minor',
//         'Moonlight Sonata|Beethoven|C# Minor',
//         'Clair de Lune|Debussy|C# Minor',
//         'Add|Sonata No.2|Chopin|B Minor',
//         'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
//         'Add|Fur Elise|Beethoven|C# Minor',
//         'Remove|Clair de Lune',
//         'ChangeKey|Moonlight Sonata|C# Major',
//         'Stop'
//     ]
// );

// solve([
//         '4',
//         'Eine kleine Nachtmusik|Mozart|G Major',
//         'La Campanella|Liszt|G# Minor',
//         'The Marriage of Figaro|Mozart|G Major',
//         'Hungarian Dance No.5|Brahms|G Minor',
//         'Add|Spring|Vivaldi|E Major',
//         'Remove|The Marriage of Figaro',
//         'Remove|Turkish March',
//         'ChangeKey|Spring|C Major',
//         'Add|Nocturne|Chopin|C# Minor',
//         'Stop'
//     ]
// );