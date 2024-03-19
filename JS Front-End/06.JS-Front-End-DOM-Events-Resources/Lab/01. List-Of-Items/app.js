function addItem() {
    const newInput = document.getElementById('newItemText').value;
    let liItem = document.createElement('li');
    liItem.textContent = newInput;
    document.querySelector('#items').appendChild(liItem);
    document.getElementById('newItemText').value = '';
}