function gradeEvaluate(grade) {
    let result = '';

    if (grade >= 5.50) {
        result = `Excellent (${grade.toFixed(2)})`;
    } else if (grade >= 4.50) {
        result = `Very good (${grade.toFixed(2)})`;
    } else if (grade >= 3.50) {
        result = `Good (${grade.toFixed(2)})`;
    } else if (grade >= 3.00) {
        result = `Poor (${grade.toFixed(2)})`;
    } else {
        result = `Fail (2)`;
    }

    console.log(result)
}

// gradeEvaluate(3.33);
// gradeEvaluate(4.50);
// gradeEvaluate(2.99);
