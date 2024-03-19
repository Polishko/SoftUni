function addItem() {
    const newInput = document.getElementById('newItemText').value;

    if (newInput.length === 0) return; // if empty input

    let liItem = document.createElement('li');
    liItem.textContent = newInput;

    let aItem = document.createElement('a');
    aItem.href = '#';
    aItem.textContent = '[Delete]'; // let linkText = document.createTextNode("[Delete]") then appendChild(linkText);
    aItem.addEventListener('click', onClick);

    liItem.appendChild(aItem);
    document.querySelector('#items').appendChild(liItem);
    document.getElementById('newItemText').value = '';

    function onClick(eventItem) {
        document.getElementById('items').removeChild(liItem);
        // or directly liItem.remove()
    }
}