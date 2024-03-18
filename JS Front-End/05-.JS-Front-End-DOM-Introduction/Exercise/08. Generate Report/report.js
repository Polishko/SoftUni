function generateReport() {
    const columnNames = document.querySelectorAll('th input');
    let selectedCols = {};
    let reportList = [];

    for (let i = 0; i < columnNames.length; i ++) {
        const col = columnNames[i];

        if (col.checked) {
            selectedCols[col.name] = i;
        }
    }

    const tableRows = document.querySelectorAll('tbody tr');

    for (const row of tableRows) {
        let rowReport = {}

        for (colName in selectedCols) {
            const targetIndex = selectedCols[colName];
            const td = row.cells[targetIndex];
            rowReport[colName] = td.textContent;
        }

        reportList.push(rowReport);
    }

    document.getElementById('output').value = JSON.stringify(reportList);
}
