function hashedWords(myString)  {
    let regexp = /#\b[A-Za-z]+\b/g;
    let myArray = myString.match(regexp);

    if (myArray) {
        myArray.forEach(word => {
            console.log(word.substring(1));
        });
    }
}


// function hashedWords(myString) {
//     let myArray = myString.split(' ');
//     let regexp = /^#[A-Za-z]+$/;


//     for (word of myArray) {
//         if (regexp.test(word)) {
//             console.log(word.substring(1));
//         }
//     }
// }

// hashedWords('Nowadays everyone uses # to tag a #special word in #socialMedia');
// hashedWords('The symbol # is known #variously in English-speaking #regions as the #number sign')
