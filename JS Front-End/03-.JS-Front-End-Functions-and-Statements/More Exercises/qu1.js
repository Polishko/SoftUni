function carCleanness(procedureList) {
    let cleanValue = 0;
    let applications = {
        'soap': (value) => value + 10,
        'water': (value) => value * 1.20,
        'vacuum cleaner': (value) => value * 1.25,
        'mud': (value) => value * 0.90, 
    }

    for (procedure of procedureList) {
        cleanValue = applications[procedure](cleanValue);
    }
    
    console.log(`The car is ${cleanValue.toFixed(2)}% clean.`);
}

// carCleanness(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water']);
// carCleanness(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"]);
