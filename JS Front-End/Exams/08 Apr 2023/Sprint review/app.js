function solve(input) {
    const num = input.shift();
    const assigneeInfo = input.slice(0, num);
    const commandInfo = input.slice(num);

    const team = assigneeInfo.reduce((acc, curr) => {
        let [assignee, taskID, title, status, estimatedPoints] = curr.split(':');
        if (!acc[assignee]) {
            acc[assignee] = [];
        }
        let task = {
          taskID,
          title,
          status,
          estimatedPoints: Number(estimatedPoints),
        };
        acc[assignee].push(task)
        return acc;
    }, {});
    // console.log(team);

    for (const item in commandInfo) {
        const [command, ...rest] = item.split(':');

        if (command === 'Add New') {
            let [assignee, taskId, title, status, estimatedPoints] = rest;
            if (!team[assignee]) {
                console.log(`Assignee ${assignee} does not exist on the board!`);
            }
            let newTask = {
                taskId,
                title,
                status,
                estimatedPoints: Number(estimatedPoints),
            };
            team[assignee].push(newTask);

        }
    }
    console.log(team);
}

solve([
        '5',
        'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
        'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
        'Peter:BOP-1211:POC:Code Review:5',
        'Georgi:BOP-1212:Investigation Task:Done:2',
        'Mariya:BOP-1213:New Account Page:In Progress:13',
        'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
        'Change Status:Peter:BOP-1290:ToDo',
        'Remove Task:Mariya:1',
        'Remove Task:Joro:1',
    ]
);

// "{assignee}:{taskId}:{title}:{status}:{estimatedPoints}".