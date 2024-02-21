function spiceExtract(yield) {
    let days = 0;
    const consumption = 26;
    let spices = 0;

    while (yield >= 100) {
        days += 1;
        spices += (yield - consumption);
        yield -= 10;

        if (yield < 100) {
            spices -= Math.min(yield, consumption);
            break;
        };
    }

    console.log(days);
    console.log(spices);
};


// spiceExtract(111);
// spiceExtract(450);