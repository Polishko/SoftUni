function encodeAndDecodeMessages() {
    const messageElements = document.querySelectorAll('#main div textarea');
    const buttonElements = document.querySelectorAll('#main div button');

    const asciiConvert = function(string, n) {
        return string.split('').map(char => {
            const code = char.charCodeAt(0);
            const shiftedCode = code + n;
            return String.fromCharCode(shiftedCode);
        }).join('');
    };

    for (let i = 0; i < buttonElements.length; i++) {
        let button = buttonElements[i]; 
        button.addEventListener('click', function(e) {
            let buttonText = button.textContent;
            let messageContent = messageElements[i].value;
            let n = (buttonText === 'Encode and send it') ? 1 : -1;
            messageElements[1].value = asciiConvert(messageContent, n);
            messageElements[0].value = '';
        }); 
    }
}
