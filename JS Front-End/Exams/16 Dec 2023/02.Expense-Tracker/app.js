window.addEventListener("load", solve);

function solve() {
    const addButton = document.getElementById('add-btn');

    addButton.addEventListener('click', function(e) {
        const previewList = document.getElementById('preview-list');
        const expensesList = document.getElementById('expenses-list');

        const allInputs = document.querySelectorAll('form.expense-content input');
        const allInputFields = Array.from(allInputs).map((element) => element.value);
        const filledFields = allInputFields.filter(element => (element !== ''));
        
        if (filledFields.length === 3) {
            previewList.innerHTML = '';

            const liPreview = document.createElement('li');
            liPreview.className = 'expense-item';
            const articleEle = document.createElement('article');
            const pType = document.createElement('p');
            pType.textContent = `Type: ${allInputFields[0]}`;
            articleEle.appendChild(pType);
            const pAmount = document.createElement('p');
            pAmount.textContent = `Amount: ${allInputFields[1]}$`;
            articleEle.appendChild(pAmount);
            const pDate = document.createElement('p');
            pDate.textContent = `Date: ${allInputFields[2]}`;
            articleEle.appendChild(pDate);
            liPreview.appendChild(articleEle);
            previewList.appendChild(liPreview);

            const buttonsDiv = document.createElement('div');
            buttonsDiv.className = 'buttons';
            const editButton = document.createElement('button');
            editButton.className = 'btn edit';
            editButton.textContent = 'edit';
            buttonsDiv.appendChild(editButton);
            const okButton = document.createElement('button');
            okButton.className = 'btn ok';
            okButton.textContent = 'ok';
            buttonsDiv.appendChild(okButton);
            liPreview.appendChild(buttonsDiv);

            addButton.disabled = true;
            Array.from(allInputs).map((input) => input.value = '');

            editButton.addEventListener('click', function(e) {
                allInputs[0].value = pType.textContent.replace('Type: ', '');
                allInputs[1].value = pAmount.textContent.replace('Amount: ', '').replace('$', '');
                allInputs[2].value = pDate.textContent.replace('Date: ', '');
                previewList.innerHTML = '';
                addButton.disabled = false;
            });

            okButton.addEventListener('click', function(e) {
                const deleteButton = document.querySelector('.btn.delete');
                const liExpense = document.createElement('li');
                liExpense.className = 'expense-item';
                liExpense.appendChild(liPreview.querySelector('article'));
                expensesList.appendChild(liExpense);
                previewList.innerHTML = '';
                addButton.disabled = false;

                deleteButton.addEventListener('click', function(e) {
                    expensesList.innerHTML = '';
                    previewList.innerHTML = '';
                    addButton.disabled = false;
                })
            });
        }
    });
}

