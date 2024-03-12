function sortArrays(inputArray) {
    let collection = new Map();

    for (element of inputArray) {
        current = JSON.parse(element)
        let sorted = current.sort((a, b) => b - a); 
        let key = JSON.stringify(sorted);       
        collection.set(key, sorted.length);
    }

    let arrayCollection = Array.from(collection);
    let sortedCollection = arrayCollection.sort((a, b) => a[1] - b[1]);

    sortedCollection.forEach((pair) => {
        let array = JSON.parse(pair[0]);
        console.log(`[${array.join(', ')}]`)
    })
}

// sortArrays(["[-3, -2, -1, 0, 1, 2, 3, 4]",
// "[10, 1, -17, 0, 2, 13]",
// "[4, -3, 3, -2, 2, -1, 1, 0]"]
// );

// sortArrays(["[7.14, 7.180, 7.339, 80.099]",
// "[7.339, 80.0990, 7.140000, 7.18]",
// "[7.339, 7.180, 7.14, 80.099]"]
// );
