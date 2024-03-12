function browserInfoLog(infoObject, actionArray) {

    for (let actionInfo of actionArray) {
        const [action, target] = actionInfo.split(' ');

        if (action === 'Open') {
            infoObject['Open Tabs'].push(target);
            infoObject['Browser Logs'].push(`Open ${target}`);
        } else if (action === 'Close') {
            let idx = infoObject['Open Tabs'].indexOf(target);

            if (idx !== -1) {
                infoObject['Recently Closed'].push(target);
                infoObject['Open Tabs'].splice(idx, 1);
                infoObject['Browser Logs'].push(`Close ${target}`);
            }
        } else {
            infoObject['Open Tabs'] = [];
            infoObject['Recently Closed'] = [];
            infoObject['Browser Logs'] = [];
        }
    }

    console.log(infoObject['Browser Name']);
    console.log(`Open Tabs: ${infoObject['Open Tabs'].join(', ')}`);
    console.log(`Recently Closed: ${infoObject['Recently Closed'].join(', ')}`);
    console.log(`Browser Logs: ${infoObject['Browser Logs'].join(', ')}`);
}

// browserInfoLog({"Browser Name":"Google Chrome","Open Tabs":["Facebook","YouTube","Google Translate"],
// "Recently Closed":["Yahoo","Gmail"],
// "Browser Logs":["Open YouTube","Open Yahoo","Open Google Translate","Close Yahoo","Open Gmail","Close Gmail","Open Facebook"]},
// ["Close Facebook", "Open StackOverFlow", "Open Google"]
// );

// browserInfoLog({"Browser Name":"Mozilla Firefox",
// "Open Tabs":["YouTube"],
// "Recently Closed":["Gmail", "Dropbox"],
// "Browser Logs":["Open Gmail", "Close Gmail", "Open Dropbox", "Open YouTube", "Close Dropbox"]},
// ["Open Wikipedia", "Clear History and Cache", "Open Twitter"]
// );
