function takeSteps(myArray, num) {
    let newArray = [];
    for (i=0; i<myArray.length; i+=num) {
        newArray.push(myArray[i]);
    }

    return newArray;
}

// takeSteps(['5', '20', '31', '4', '20'], 2);
// takeSteps(['dsa','asd', 'test', 'tset'], 2);
// takeSteps(['1', '2','3', '4', '5'], 6);