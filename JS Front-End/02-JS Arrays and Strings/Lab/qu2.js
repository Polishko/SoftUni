function reverseArray(num, myArray) {
    let newArray = myArray.slice(0, num).reverse();

    console.log(newArray.join(' '));
}
