function colorize() {
    let table = document.querySelectorAll('table tr:not(:first-of-type)');

    for (let i = 0; i < table.length; i += 2) {
        let row = table[i];
        row.style.background = 'Teal';
    }
}