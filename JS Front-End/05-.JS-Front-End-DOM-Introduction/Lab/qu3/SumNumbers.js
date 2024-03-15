
function calc() {
    let numA = document.getElementById('num1').value;
    let numB = document.getElementById('num2').value;
    let sum = Number(numA) + Number(numB);

    document.getElementById('sum').value = sum;
}


// function calc() {
//     let num1 = document.getElementById('num1');
//     let num2 = document.getElementById('num2');
//     let sum = Number(num1.value) + Number(num2.value);

//     document.getElementById('sum').value = sum;
// }