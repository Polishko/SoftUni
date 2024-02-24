function findTemplate(words, mainString) {
    let keyWords = words.split(', ');
    let stringArray = mainString.split(' ');

    for (template of keyWords) {
        for (let i = 0; i < stringArray.length; i++) {
            let current = stringArray[i];
            if (current.includes('*') && current.length === template.length) {
                 stringArray.splice(i, 1, template);
            }
        }
    }

    console.log(stringArray.join(' '));
}


// findTemplate('great', 'softuni is ***** place for learning new programming languages');
// findTemplate('great, learning', 'softuni is ***** place for ******** new programming languages');

