function studentArrange(inputArray) {
    let studentInformation = {};

    for (let info of inputArray) {
        const [studentInfo, gradeInfo, scoreInfo] = info.split(', ');
        const name = studentInfo.split(': ')[1];
        const grade = parseInt(gradeInfo.split(': ')[1]) + 1;
        const score = parseFloat(scoreInfo.split(': ')[1]);

        if (score < 3) {
            continue;
        }

        if (!(studentInformation.hasOwnProperty(grade))) {
            studentInformation[grade] = {
                students: [],
                gradeSum: 0,
            };
        }

        studentInformation[grade].students.push(name);
        studentInformation[grade].gradeSum += score;
    }

    const sortedStudents = Object.entries(studentInformation).sort((a, b) => a[0] - b[0]);

    for (let i = 0; i < sortedStudents.length; i++) {
        const record = sortedStudents[i];
        const studentList = record[1].students.join(', ');
        const aveGrades = record[1].gradeSum / record[1].students.length;

        console.log(`${record[0]} Grade`);
        console.log(`List of students: ${studentList}`);
        console.log(`Average annual score from last year: ${aveGrades.toFixed(2)}`);

        if (i !== sortedStudents.length - 1) {
            console.log();
        }
    }
}

// studentArrange([
//     "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
//         "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
//         "Student name: George, Grade: 8, Graduated with an average score: 2.83",
//         "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
//         "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
//         "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
//         "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
//         "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
//         "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
//         "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
//         "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
//         "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00"
//     ]
//     );

// studentArrange([
//     'Student name: George, Grade: 5, Graduated with an average score: 2.75',
//     'Student name: Alex, Grade: 9, Graduated with an average score: 3.66',
//     'Student name: Peter, Grade: 8, Graduated with an average score: 2.83',
//     'Student name: Boby, Grade: 5, Graduated with an average score: 4.20',
//     'Student name: John, Grade: 9, Graduated with an average score: 2.90',
//     'Student name: Steven, Grade: 2, Graduated with an average score: 4.90',
//     'Student name: Darsy, Grade: 1, Graduated with an average score: 5.15'
//     ]
//     );