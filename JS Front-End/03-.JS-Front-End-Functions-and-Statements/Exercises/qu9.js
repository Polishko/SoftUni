function loadingBar(num) {
    if (num % 100 === 0) {
        console.log(`100% Complete!`);
        console.log(`[%%%%%%%%%%]`);
    } else {
        let percents = '%'.repeat(num / 10);
        let dots = '.'.repeat(10 - (num / 10));
        console.log(`${num}% [${percents}${dots}]`);
        console.log(`Still loading...`)
    }
}

// loadingBar(30);
// loadingBar(50);
// loadingBar(100);