function solve() {
  const generateButton = document.querySelector('#exercise button:nth-of-type(1)');
  const buyButton = document.querySelector('#exercise button:nth-of-type(2)');
  const boxes = document.querySelectorAll('tbody td input'); 

  generateButton.addEventListener('click', function(e) {
    const tableBody = document.querySelector('tbody');
    const arrayObjectsElement = document.querySelector('#exercise textarea:nth-of-type(1)').value;
    const productObjects = JSON.parse(arrayObjectsElement);
       
    Array.from(boxes).map((box) => {
      if (box.disabled === true) {
        box.disabled = false;
      }
    });
    
    for (let productObj of productObjects) {
      let product = Object.entries(productObj);
      let newRow = document.createElement('tr');

      for (i = 0; i < 5; i++) {
        let newColumn = document.createElement('td');
        newRow.appendChild(newColumn);
      }

      for (item of product) {
        let attr = item[0];
        let value = item[1];
        let newEle;

        if (attr === 'img') {
          newEle = document.createElement('img');
          newEle.src = value;
          newRow.querySelector('td:nth-of-type(1)').appendChild(newEle);
        } else {
          newEle = document.createElement('p');
          newEle.textContent = value;
          switch (attr) {
            case 'name':
              newRow.querySelector('td:nth-of-type(2)').appendChild(newEle);
              break;
            case 'price':
              newRow.querySelector('td:nth-of-type(3)').appendChild(newEle);
              break;
            case 'decFactor':
              newRow.querySelector('td:nth-of-type(4)').appendChild(newEle);
          }
        }
      }
      
      let checkBoxEle = document.createElement('input');
      checkBoxEle.type = 'checkbox';
      checkBoxEle.disabled = false;
      newRow.querySelector('td:nth-of-type(5)').appendChild(checkBoxEle);
      tableBody.appendChild(newRow);
    }
  });

  buyButton.addEventListener('click', function(e) {
    let purchasedProducts = [];
    let sumPrice = 0;
    let sumFactors = 0;
    const allRows = document.querySelectorAll('tbody tr');
    let secondTextArea = document.querySelector('#exercise textarea:nth-of-type(2)');
    secondTextArea.disabled = false;
    
    for (row of allRows) {
      const rowTD = row.querySelectorAll('td');
      if (rowTD[4].querySelector('input').checked === true) {
        const name = rowTD[1].querySelector('p').textContent;
        const price = Number(rowTD[2].querySelector('p').textContent);
        const factor = Number(rowTD[3].querySelector('p').textContent);

        purchasedProducts.push(name);
        sumPrice += price;
        sumFactors += factor;
      }
    }

    let result1 = `Bought furniture: ${purchasedProducts.join(', ')}\n`;
    let result2 = `Total price: ${sumPrice.toFixed(2)}\n`;
    let result3 = `Average decoration factor: ${sumFactors / purchasedProducts.length}`;
    secondTextArea.value = (result1 + result2 + result3);
  });
}


// function solve() {
  
//   // console.log(arrayObjectsElement)
//   const generateButton = document.querySelector('#exercise button:nth-of-type(1)');
//   // console.log(generateButton.textContent)
//   // const tableBody = document.querySelector('tbody');

//   generateButton.addEventListener('click', function(e) {
//     const arrayObjectsElement = document.querySelector('#exercise textarea:nth-of-type(1)').value;
//     let secondTextArea = document.querySelector('#exercise textarea:nth-of-type(2)');
//     secondTextArea.disabled = false;
//     secondTextArea.value = arrayObjectsElement;
//   });
// }
