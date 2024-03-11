function listSongs(inputArray) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    const [count, ...songsAndType] = inputArray;
    const [songs, type] = [songsAndType.slice(0, songsAndType.length - 1), songsAndType[songsAndType.length - 1]];

    let songsList = [];
    for (let info of songs) {
        const [typeList, name, time] = info.split('_');
        songsList.push(new Song(typeList, name, time));
    }

    let printList;
    if (type === 'all') {
        printList = songsList.slice();
    } else {
        printList = songsList.filter((song) => song.typeList === type);
    }
    
    printList.forEach((songObject) => console.log(`${songObject.name}`));
}


// listSongs([3,
//     'favourite_DownTown_3:14',
//     'favourite_Kiss_4:16',
//     'favourite_Smooth Criminal_4:01',
//     'favourite']
//     );

// listSongs([4,
//     'favourite_DownTown_3:14',
//     'listenLater_Andalouse_3:24',
//     'favourite_In To The Night_3:58',
//     'favourite_Live It Up_3:48',
//     'listenLater']
//     );

// listSongs([2,
//     'like_Replay_3:15',
//     'ban_Photoshop_3:48',
//     'all']
//     );
