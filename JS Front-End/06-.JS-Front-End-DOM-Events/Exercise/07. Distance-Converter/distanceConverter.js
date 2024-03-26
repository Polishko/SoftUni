function attachEventsListeners() {
    const convertButton = document.querySelector('#convert');

    convertButton.addEventListener('click', function(e) {
        const inputDistance = document.querySelector('#inputDistance');
        const outputDistance = document.querySelector('#outputDistance');

        const inputIdx = document.querySelector('#inputUnits').selectedIndex;
        const outputIdx = document.querySelector('#outputUnits').selectedIndex;

        conversionConstants = new Map([
            [0, 1000],
            [1, 1],
            [2, 0.01],
            [3, 0.001],
            [4, 1609.34],
            [5, 0.9144],
            [6, 0.3048],
            [7, 0.0254],
        ]);

        outputDistance.disabled = false;
        outputDistance.value = inputDistance.value * conversionConstants.get(inputIdx) / conversionConstants.get(outputIdx); 
    })
}
