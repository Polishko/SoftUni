function calculateExpenses(lostFights, helmet, sword, shield, repair) {

    let priceHelmet = Math.trunc(lostFights / 2) * helmet;
    let priceSword = Math.trunc(lostFights / 3) * sword;
    let priceShield = Math.trunc(lostFights / 6) * shield;
    let priceRepair = Math.trunc(lostFights / 12) * repair;

    let totalPrice = priceHelmet + priceSword + priceShield + priceRepair;

    console.log(`Gladiator expenses: ${totalPrice.toFixed(2)} aureus`);
}

// calculateExpenses(7, 2, 3, 4, 5);
// calculateExpenses(23, 12.5, 21.5, 40, 200);