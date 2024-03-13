function getArmyInfo(inputArray) {
    const armyLog = {};
    
    for (info of inputArray) {
        if (info.includes('arrives')) {
            
            let leader = info.replace(' arrives', '');
            if (!armyLog.hasOwnProperty(leader)) {
                armyLog[leader] = {};
            }
            
        } else if (info.includes(':')) {

            let [leader, armyInfo] =info.split(': ');           
            if (armyLog.hasOwnProperty(leader)) {
                let [army, num] = armyInfo.split(', ');
                armyLog[leader][army] = parseInt(num);
            }
                
        } else if (info.includes('+')) {
            let [army, num] = info.split(' + ');

            for (let key of Object.keys(armyLog)) {
                if (armyLog[key].hasOwnProperty(army)) {
                    armyLog[key][army] += parseInt(num);
                    break;
                }
            }
        } else if (info.includes('defeated')) {
            let leader = info.replace(' defeated', '');
            delete armyLog[leader];
        }
    }

    const leaderTotals = {};
    for (leader of Object.keys(armyLog)) {
        const total = Object.values(armyLog[leader]).reduce((acc, curr) => acc + curr, 0);
        leaderTotals[leader] = total;
    }
    
    const sortedTotals = Object.entries(leaderTotals).sort((a, b) => b[1] - a[1]);

    for (leaderDetails of sortedTotals) {
        let [leader, total] = [leaderDetails[0], leaderDetails[1]];
        console.log(`${leader}: ${total}`);
        const armies = Object.entries(armyLog[leader]).sort((a, b) => b[1] - a[1]);
        armies.forEach((armyDetail) => console.log(`>>> ${armyDetail[0]} - ${armyDetail[1]}`));
    }
}


// getArmyInfo(['Rick Burr arrives',
//  'Fergus: Wexamp, 30245',
//   'Rick Burr: Juard, 50000', 'Findlay arrives',
//    'Findlay: Britox, 34540', 'Wexamp + 6000', 'Juard + 1350',
//     'Britox + 4500', 'Porter arrives', 'Porter: Legion, 55000',
//      'Legion + 302', 'Rick Burr defeated', 'Porter: Retix, 3205']);

getArmyInfo(['Rick Burr arrives', 'Findlay arrives',
 'Rick Burr: Juard, 1500', 'Wexamp arrives',
  'Findlay: Wexamp, 34540', 'Wexamp + 340',
   'Wexamp: Britox, 1155', 'Wexamp: Juard, 43423']);
