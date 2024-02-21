function isValidDistance(x1, y1, x2, y2) {
    let points = [`{${x1}, ${y1}} to {0, 0}`, `{${x2}, ${y2}} to {0, 0}`, `{${x1}, ${y1}} to \{${x2}, ${y2}}`]
    let distances = [Math.sqrt(x1**2 + y1**2), Math.sqrt(x2**2 + y2**2), Math.sqrt((x2-x1)**2 + (y2-y1)**2)];

    let result;
    for (let i=0; i < 3; i++) {
        result = (distances[i] % 10).toString().length;
        let status = (result > 1) ? 'invalid' : 'valid'
        console.log(`${points[i]} is ${status}`)
    }
}


// isValidDistance(3, 0, 0, 4);
// isValidDistance(2, 1, 1, 1);
