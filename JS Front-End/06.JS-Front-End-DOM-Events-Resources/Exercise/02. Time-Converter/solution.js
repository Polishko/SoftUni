function attachEventsListeners() {
    let buttonItems = document.querySelectorAll('input[type="button"]');
    let inputItems = document.querySelectorAll('input[type="text"]');

    const conversionArray = {
        'days': 1,
        'hours': 24,
        'minutes': 1440,
        'seconds': 86400,
    }

    for (let button of buttonItems) {
        button.addEventListener('click', function(e) {
            const targetID = button.id.replace('Btn', '');
            const inputValue = Number(document.getElementById(targetID).value);

            if (!isNaN(inputValue)) {
                const factor = inputValue / conversionArray[targetID];

            Array.from(inputItems).forEach(item => {
                if (!item.value) {
                    const itemID = item.id;
                    item.value = factor * conversionArray[itemID];
                }
            });
            }
        });
    }   

    for (let input of inputItems) {
        input.addEventListener('input', function(e) {
            const inputValue = Number(input.value);
            if (!isNaN(inputValue)) {
                Array.from(inputItems).forEach(item => {
                    if (item !== input) {
                        item.value = '';
                    }
                });
            }
        });
    }
}