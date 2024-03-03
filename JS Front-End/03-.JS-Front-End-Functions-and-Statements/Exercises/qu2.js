function sumAndSubstract(num1, num2, num3) {
    let result = sum(num1, num2) - num3;

    function sum(a, b) {
        return a + b;
    }

    console.log(result);
}

// sumAndSubstract(23, 6, 10);
// sumAndSubstract(1, 17, 30);
// sumAndSubstract(42, 58, 100);