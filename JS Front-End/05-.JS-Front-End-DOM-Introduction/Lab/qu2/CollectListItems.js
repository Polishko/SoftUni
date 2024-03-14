function extractText() {
    let allNodes = document.querySelectorAll('#items li');
    let textArea = document.querySelector('#result');

    for (let node of allNodes) {
        // @ts-ignore
        textArea.value += node.textContent + '\n'
    }
}

