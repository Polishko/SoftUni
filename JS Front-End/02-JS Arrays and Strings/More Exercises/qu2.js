function miningBitcoins(minedGold) {
    const priceGramGold = 67.51;
    const priceBitcoin = 11949.16;
    let dayOfFirstBitcoinPurchase;
    let firstBitcoinPurchased = false;
    let earnedMoney = 0;
    let totalBitcoins = 0;

    for (let i = 0; i < minedGold.length; i++) {
        let digged = minedGold[i];
        let dailyMoney = digged * priceGramGold;

        if ((i + 1) % 3 === 0) {
            dailyMoney *= 0.7;
        }

        earnedMoney += dailyMoney;

        if (earnedMoney >= priceBitcoin) {
            let dailyBitcoins =  Math.floor(earnedMoney / priceBitcoin);
            earnedMoney -= (dailyBitcoins * priceBitcoin);
            totalBitcoins += dailyBitcoins;

            if (firstBitcoinPurchased === false) {
                dayOfFirstBitcoinPurchase = i + 1;
                firstBitcoinPurchased = true;
            }
        }
    }
    console.log(`Bought bitcoins: ${totalBitcoins}`);
    if (dayOfFirstBitcoinPurchase) {
        console.log(`Day of the first purchased bitcoin: ${dayOfFirstBitcoinPurchase}`);
    }
    console.log(`Left money: ${earnedMoney.toFixed(2)} lv.`)
}


// miningBitcoins([50, 100]);
// miningBitcoins([3124.15, 504.212, 2511.124]);