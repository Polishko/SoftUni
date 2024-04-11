function solve(input) {
    const num = input.shift();
    const assigneeInfo = input.slice(0, num);
    const commandInfo = input.slice(num);

    let toDoTasksTotalPoints = 0;
    let inProgressTasksTotalPoints = 0;
    let codeReviewTasksTotalPoints = 0;
    let doneTasksTotalPoints = 0;

    const team = assigneeInfo.reduce((acc, curr) => {
        let [assignee, taskId, title, status, estimatedPoints] = curr.split(':');
        if (!acc[assignee]) {
            acc[assignee] = [];
        }
        let task = {
          taskId: taskId,
          title,
          status,
          estimatedPoints: Number(estimatedPoints),
        };
        acc[assignee].push(task)
        return acc;
    }, {});
    // console.log(team);

    for (const item of commandInfo) {
        const commands = item.split(':');
        const command = commands.shift();

        if (command === 'Add New') {
            let [assignee, taskId, title, status, estimatedPoints] = commands;
            if (!team[assignee]) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            } else {
                let newTask = {
                    taskId,
                    title,
                    status,
                    estimatedPoints: Number(estimatedPoints),
                };
                team[assignee].push(newTask);
            }


        } else if (command === 'Change Status') {
            let [assignee, taskId, newStatus] = commands;
            if (!team[assignee]) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            } else {
                let taskFound = false;
                for (const task of team[assignee]) {
                    if (task.taskId === taskId) {
                        task.status = newStatus;
                        taskFound = true;
                        break;
                    }
                }
                if (taskFound === false) {
                    console.log(`Task with ID ${taskId} does not exist for ${assignee}!`)
                }
            }
        } else if (command === 'Remove Task') {
            let [assignee, indexStr] = commands;
            let index = Number(indexStr);
            if (!team[assignee]) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            } else if (index < 0 || index >= team[assignee].length) {
                console.log(`Index is out of range!`)
            } else {
                team[assignee].splice(index, 1);
            }
        }
    }

    for (const array of Object.values(team)) {
        toDoTasksTotalPoints += array.filter(task => task.status === 'ToDo').reduce((acc, curr) => acc + curr.estimatedPoints, 0);
        inProgressTasksTotalPoints += array.filter(task => task.status === 'In Progress').reduce((acc, curr) => acc + curr.estimatedPoints, 0);
        codeReviewTasksTotalPoints += array.filter(task => task.status === 'Code Review').reduce((acc, curr) => acc + curr.estimatedPoints, 0);
        doneTasksTotalPoints += array.filter(task => task.status === 'Done').reduce((acc, curr) => acc + curr.estimatedPoints, 0);
    }

    console.log(`ToDo: ${toDoTasksTotalPoints}pts`);
    console.log(`In Progress: ${inProgressTasksTotalPoints}pts`);
    console.log(`Code Review: ${codeReviewTasksTotalPoints}pts`);
    console.log(`Done Points: ${doneTasksTotalPoints}pts`);

    if (doneTasksTotalPoints >= (toDoTasksTotalPoints + inProgressTasksTotalPoints + codeReviewTasksTotalPoints)) {
        console.log('Sprint was successful!');
    } else {
        console.log('Sprint was unsuccessful...');
    }
}

// solve([
//         '5',
//         'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
//         'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
//         'Peter:BOP-1211:POC:Code Review:5',
//         'Georgi:BOP-1212:Investigation Task:Done:2',
//         'Mariya:BOP-1213:New Account Page:In Progress:13',
//         'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
//         'Change Status:Peter:BOP-1290:ToDo',
//         'Remove Task:Mariya:1',
//         'Remove Task:Joro:1',
//     ]
// );

solve([
        '4',
        'Kiril:BOP-1213:Fix Typo:Done:1',
        'Peter:BOP-1214:New Products Page:In Progress:2',
        'Mariya:BOP-1215:Setup Routing:ToDo:8',
        'Georgi:BOP-1216:Add Business Card:Code Review:3',
        'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
        'Change Status:Georgi:BOP-1216:Done',
        'Change Status:Will:BOP-1212:In Progress',
        'Remove Task:Georgi:3',
        'Change Status:Mariya:BOP-1215:Done',
    ]
);