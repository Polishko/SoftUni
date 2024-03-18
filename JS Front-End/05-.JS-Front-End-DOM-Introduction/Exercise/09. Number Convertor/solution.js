function solve() {
    const hexadecimalOption = document.createElement('option');
    hexadecimalOption.value = 'hexadecimal';
    hexadecimalOption.textContent = 'Hexadecimal';
    document.getElementById('selectMenuTo').appendChild(hexadecimalOption);

    const binaryOption = document.createElement('option');
    binaryOption.value = 'binary';
    binaryOption.textContent = 'Binary';
    document.getElementById('selectMenuTo').appendChild(binaryOption);

    const convertButton = document.querySelector('button');

    convertButton.addEventListener('click', () => {     
        document.getElementById('result').disabled = false;

        let inputNum = Number(document.getElementById('input').value);
        const option = document.getElementById('selectMenuTo').value;

        let digits = [];
        const divisor = (option === 'hexadecimal') ? 16 : 2;

        const convertNum = (num) => {
            let quotient = parseInt(num / divisor);
            let remainder = num % divisor;

            if (quotient === 0) {
                digits.push(remainder);
                return digits.reverse().join('');
            }

            if (option === 'hexadecimal' && remainder >= 10) {
                const letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'};
                remainder = letters[remainder];
            }

            digits.push(remainder);
            return convertNum(quotient);
        }

        document.getElementById('result').value = convertNum(inputNum);       
        
    });
}