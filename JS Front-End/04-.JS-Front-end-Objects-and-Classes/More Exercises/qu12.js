function getStudentCourses(inputArray) {
    const courseList = {};
    const allData = {};

    for (info of inputArray) {
        if (info.includes(':')) {
            let [courseName, capacity] = info.split(': ');

            if (!courseList.hasOwnProperty(courseName)) {
                courseList[courseName] = 0;
            }

            if (!allData.hasOwnProperty(courseName)) {
                allData[courseName] = [];
            }

            courseList[courseName] += parseInt(capacity);
        } else {
            const regex = /(\w+)\[(\d+)\] with email (\S+) joins (.+)/;
            const match = regex.exec(info);
            const [, userName, credits, email, courseName] = match;

            if (courseList.hasOwnProperty(courseName) && courseList[courseName] > 0) {
                allData[courseName].push([parseInt(credits), `${userName}, ${email}`]);
                courseList[courseName] -= 1;
            }
        }
    }

    const sortedData = Object.entries(allData).sort((a, b) => {
        const studentCountA = a[1].length;
        const studentCountB = b[1].length;
        return studentCountB - studentCountA;
    })

    for ([course, listings] of sortedData) {
        let places = courseList[course];
        let allUsers = listings.sort((a, b) => b[0] - a[0]);
        console.log(`${course}: ${places} places left`);
        allUsers.forEach((user) => console.log(`--- ${user[0]}: ${user[1]}`));
    }
}

getStudentCourses(['JavaBasics: 2', 'user1[25] with email user1@user.com joins C#Basics', 'C#Advanced: 3', 'JSCore: 4', 'user2[30] with email user2@user.com joins C#Basics', 'user13[50] with email user13@user.com joins JSCore', 'user1[25] with email user1@user.com joins JSCore', 'user8[18] with email user8@user.com joins C#Advanced', 'user6[85] with email user6@user.com joins JSCore', 'JSCore: 2', 'user11[3] with email user11@user.com joins JavaBasics', 'user45[105] with email user45@user.com joins JSCore', 'user007[20] with email user007@user.com joins JSCore', 'user700[29] with email user700@user.com joins JSCore', 'user900[88] with email user900@user.com joins JSCore']);

// getStudentCourses(['JavaBasics: 15',
// 'user1[26] with email user1@user.com joins JavaBasics',
// 'user2[36] with email user11@user.com joins JavaBasics',
// 'JavaBasics: 5',
// 'C#Advanced: 5',
// 'user1[26] with email user1@user.com joins C#Advanced',
// 'user2[36] with email user11@user.com joins C#Advanced',
// 'user3[6] with email user3@user.com joins C#Advanced',
// 'C#Advanced: 1',
// 'JSCore: 8',
// 'user23[62] with email user23@user.com joins JSCore']
// );