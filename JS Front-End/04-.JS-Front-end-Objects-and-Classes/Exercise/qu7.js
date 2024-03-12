function findOddOccurrences(inputString) {
    const elements = new Map();
    const inputArray = inputString.split(' ');

    for (let item of inputArray) {
        let element = item.toLocaleLowerCase();
        elements.set(element, (elements.get(element) || 0) + 1);
    }

    const oddOccurrences = []
    elements.forEach((count, element) => {
        if (count % 2 == 1) {
            oddOccurrences.push(element);
        }
    })

    console.log(oddOccurrences.join(' '));
}


// findOddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
// findOddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');

