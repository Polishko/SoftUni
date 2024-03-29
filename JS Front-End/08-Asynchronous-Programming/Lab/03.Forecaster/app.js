function attachEvents() {
    BASE_URL = 'http://localhost:3030/jsonstore/forecaster/';
    const buttonElement = document.getElementById('submit');
    const locationInput = document.getElementById('location');
    const mainForecastDiv = document.getElementById('forecast');
    let locationCode;
    let location;
    let lowT;
    let highT;
    let condition;

    const symbols = {
        'Sunny': '&#x2600;',
        'Partly sunny': '&#x26C5;',
        'Overcast': '&#x2601;',
        'Rain': '&#x2614;',
        'Degrees': '&#176;',
    }

    const displayError = function() {
        mainForecastDiv.style.display = 'block';
        mainForecastDiv.textContent = 'Error';
    };

    buttonElement.addEventListener('click', function(e) {
        mainForecastDiv.style.display = 'block';

        fetch(`${BASE_URL}locations`)
        .then((response) => response.json())
        .then((array) => {
            
            const locationObj = array.find((obj) => obj.name === locationInput.value);
            locationCode = locationObj.code;
            location = locationObj.name;
            
        //  Current
            fetch(`${BASE_URL}today/${locationCode}`)
            .then((response) => response.json())
            .then((obj) => {
                [location, lowT, highT, condition] = [obj.name, obj.forecast.low, obj.forecast.high, obj.forecast.condition];

                const currentDiv = document.getElementById('current');

                const forecastsDiv = document.createElement('div');
                forecastsDiv.className = 'forecasts';

                const spanSymb = document.createElement('span');
                spanSymb.className = 'condition symbol';
                spanSymb.innerHTML = symbols[condition];

                const spanMainCond = document.createElement('span');
                spanMainCond.className = 'condition';

                const spanLoc = document.createElement('span');
                spanLoc.className = 'forecast-data';
                spanLoc.textContent = location; 
                const spanTemp = document.createElement('span');
                spanTemp.className = 'forecast-data';
                spanTemp.innerHTML = `${lowT}${symbols['Degrees']}/${highT}${symbols['Degrees']}`; 
                const spanCond = document.createElement('span');
                spanCond.className = 'forecast-data';
                spanCond.textContent = condition;

                spanMainCond.appendChild(spanLoc);
                spanMainCond.appendChild(spanTemp);
                spanMainCond.appendChild(spanCond);

                forecastsDiv.appendChild(spanSymb);
                forecastsDiv.appendChild(spanMainCond);
                currentDiv.appendChild(forecastsDiv);
                })
                .catch((e) => displayError())

            // 3-Day
            fetch(`${BASE_URL}upcoming/${locationCode}`)
            .then((response) => response.json())
            .then((obj) => {
                const days = obj.forecast;
                const upcomingDiv = document.getElementById('upcoming');

                const forecastInfoDiv = document.createElement('div');
                forecastInfoDiv.className = 'forecast-info';

                for (oneDay of days) {  
                    [lowT, highT, condition] = [oneDay.low, oneDay.high, oneDay.condition];
                    const spanUpcoming = document.createElement('span');
                    spanUpcoming.className ='upcoming';

                    const symbolSpan = document.createElement('span');
                    symbolSpan.className = 'symbol';
                    symbolSpan.innerHTML = symbols[condition];
                    spanUpcoming.appendChild(symbolSpan);

                    const spanTemp = document.createElement('span');
                    spanTemp.className = 'forecast-data';
                    spanTemp.innerHTML = `${lowT}${symbols['Degrees']}/${highT}${symbols['Degrees']}`;
                    spanUpcoming.appendChild(spanTemp);

                    const spanCond = document.createElement('span');
                    spanCond.className = 'forecast-data';
                    spanCond.textContent = condition;
                    spanUpcoming.appendChild(spanCond);

                    forecastInfoDiv.appendChild(spanUpcoming);
                }
                
                upcomingDiv.appendChild(forecastInfoDiv);
            })
            .catch((e) => displayError())
        })
        .catch((e) => displayError())                   
    });//button event listener
}

attachEvents();