function pointValidation(pointArray) {
    let [x1, y1, x2, y2] = pointArray;

    let validationStep = function(a1, b1, a2, b2) {
        let distance = Math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2);
        let points = `{${a1}, ${b1}} to {${a2}, ${b2}}`

        return (Number.isInteger(distance)) ? `${points} is valid` : `${points} is invalid`;
    }

    console.log(validationStep(x1, y1, 0, 0));
    console.log(validationStep(x2, y2, 0, 0));
    console.log(validationStep(x1, y1, x2, y2));
}

// pointValidation([3, 0, 0, 4]);
pointValidation([2, 1, 1, 1]);