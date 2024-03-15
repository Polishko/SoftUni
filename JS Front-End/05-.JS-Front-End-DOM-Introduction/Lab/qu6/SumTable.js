function sumTable() {
    let table = document.getElementsByTagName('table')[0];
    let lastColumn = table.querySelectorAll('td:last-child');

    let sum = 0;
    for (i = 0; i < lastColumn.length; i++) {
        let element = lastColumn[i];

        if (i === lastColumn.length - 1) {
            element.textContent = sum;
            break;
        }

        sum += Number(element.textContent);
    }
}