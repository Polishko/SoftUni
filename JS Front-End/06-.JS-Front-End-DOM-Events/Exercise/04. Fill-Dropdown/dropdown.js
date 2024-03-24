function addItem() {
    const textField = document.querySelector('#newItemText');
    const valueField = document.querySelector('#newItemValue');
    const button = document.querySelector('input[value=Add]');
    const menu = document.querySelector('#menu');
    const option = document.createElement('option');
    option.textContent = textField.value;
    option.value = valueField.value;
    menu.appendChild(option);
    textField.value = '';
    valueField.value = '';        
}

