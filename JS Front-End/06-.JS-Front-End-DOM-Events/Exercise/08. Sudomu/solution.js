function solve() {
    const checkButton = document.querySelectorAll('button')[0];
    const clearButton = document.querySelectorAll('button')[1];
    const allRows = document.querySelectorAll('tbody tr');
    const tableElement = document.querySelector('table');
    const resultDiv = document.querySelector('#check p');

    const isLineValid = function(tdArray) {
        const set = new Set();
        tdArray.forEach(td => {
            const input = td.querySelector('input');
            if (input.value >= input.min && input.value <= input.max) {
                set.add(input.value);
            }
        })
        return set.size === 3; 
    };

    const getAllTd = function(rowArray) {
        const allTdArrays = [];
        
        // horizontal
        Array.from(allRows).forEach(row => {
            const horizontal = Array.from(row.querySelectorAll('td'));
            allTdArrays.push(horizontal);
        })

        // vertical
        for (let i = 0; i < 3; i++) {
            const vertical = [];

            Array.from(allRows).forEach(row => {
                vertical.push(row.querySelectorAll('td')[i]);
            })

            allTdArrays.push(vertical);
        }

        return allTdArrays;
    };

    const isGameWon = function(tdArray) {
        let won = 'true';
        for (item of tdArray) {
            if (!isLineValid(item)) {
                won = 'false';
                break;
            }
        }

        return won;
    };

    const tableStyle = function(result) {
        if (result === 'true') {
            tableElement.style.border = '2px solid green';
            resultDiv.textContent = 'You solve it! Congratulations!';
            resultDiv.style.color = 'green';
        } else if (result === 'false') {
            tableElement.style.border = '2px solid red';
            resultDiv.textContent = 'NOP! You are not done yet...';
            resultDiv.style.color = 'red';
        } else if (result === 'clear') {
            tableElement.style.border = 'none';
            resultDiv.textContent = '';
            resultDiv.style.color = 'none';
        }
    };

    checkButton.addEventListener('click', function(e) { 
        tableStyle(isGameWon(getAllTd(allRows)));     
    });

    clearButton.addEventListener('click', function(e) {
        Array.from(document.querySelectorAll('tbody td input')).forEach(item => {
            item.value = '';
        });
        tableStyle('clear');
    });
}
