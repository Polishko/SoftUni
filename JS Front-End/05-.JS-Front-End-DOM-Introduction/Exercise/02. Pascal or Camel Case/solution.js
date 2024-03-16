function solve() {
  let param1 = document.getElementById('text').value;
  let param2 = document.getElementById('naming-convention').value;
  let AllWords = param1.split(' ').map((word) => word.toLowerCase());
  let firstWord = AllWords.shift();
  let result = firstWord;

  if (param2 === 'Pascal Case') {   
    result = firstWord[0].toUpperCase() + firstWord.slice(1);
  } else if (param2 !== 'Camel Case') {
    result = 'Error!'
  }

  if (result !== 'Error!') {
    for (let word of AllWords) {
      word = word[0].toUpperCase() + word.slice(1);
      result += word;
    }
  }
  
  let spanElement = document.getElementById('result');
  spanElement.textContent = result;

}
