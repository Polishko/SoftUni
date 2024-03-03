function cristalProcess(inputArray) {
    let target = inputArray[0];
    chunks = inputArray.slice(1);

    let mainProcesses = {
        'Cut': (value) => value / 4,
        'Lap': (value) => value * 0.8,
        'Grind': (value) => value - 20,
        'Etch': (value) => value - 2,
    };

    let getTreatments = (amount, processes) => {
        return Object.entries(processes)
            .map(([key, func]) => ({ name: key, value: func(amount) }))
            .sort((a, b) => a.value - b.value);
    };

    let processChunk = (amount) => {
        let xRayNeeded = false;
        let copyProcesses = { ...mainProcesses };
        let operations = [];

        while (amount !== target) {
            let treatments = getTreatments(amount, copyProcesses);      
            let treatment = treatments[0];
            if (!treatment) break;
            
            let count = 0;     
            while (copyProcesses[treatment.name](amount) >= target - 1) {
                amount = copyProcesses[treatment.name](amount);
                count += 1;

                if (amount === target || amount === target - 1) {
                    break;
                }
            }

            if (amount === target - 1) {
                xRayNeeded = true;
            }

            if (count > 0) {
                operations.push({ name: treatment.name, count });
            }

            delete copyProcesses[treatment.name];          
        }

        return { operations, xRayNeeded};
    };

    for (let amount of chunks) {
        console.log(`Processing chunk ${amount} microns`);
        let { operations, xRayNeeded } = processChunk(amount);
        
        operations.forEach(oper => {
            console.log(`${oper.name} x${oper.count}`);
            console.log('Transporting and washing');
        });

        if (xRayNeeded) {
            console.log('X-ray x1');
        }

        console.log(`Finished crystal ${target} microns`);
    }
}

// cristalProcess([1375, 50000]);
// cristalProcess([1000, 4000, 8100]);