function listUserComments(inputArray) {
    const articleList = [];
    const userList =[];
    const allArticles = {};

    function addToList(item, target, list) {
        target = item;
        list.push(item);
    }

    for (string of inputArray) {
        if (string.includes(':')) {
            const [part1, part2] = string.split(': ');
            let [userName, articleName] = part1.split(' posts on ');
            let [commentTitle, commentContent] = part2.split(', ')

            if (userList.includes(userName) && articleList.includes(articleName)) {

                if (!allArticles.hasOwnProperty(articleName)) {
                    allArticles[articleName] = [];
                }               
                allArticles[articleName].push([userName, `${commentTitle} - ${commentContent}`]);
            }

        } else {
            const [item1, item2] = string.split(' ');
            let userName, articleName;
            string.startsWith('user ') ? addToList(item2, userName, userList) : addToList(item2, articleName, articleList);
        }
    }

    sortedArticles = Object.entries(allArticles).sort((a, b) => {
        const arrayA = a[1].length;
        const arrayB = b[1].length;
        return arrayB - arrayA;
    })

    for (let article of sortedArticles) {
        let [name, contentList] = [article[0], article[1]] 
        console.log(`Comments on ${name}`);
        let sortedContent = contentList.sort((a, b) => a[0].localeCompare(b[0]));
        sortedContent.forEach((item) => console.log(`--- From user ${item[0]}: ${item[1]}`));
    }
}

// listUserComments(['user aUser123', 'someUser posts on someArticle: NoTitle, stupidComment',
//  'article Books', 'article Movies', 'article Shopping', 'user someUser',
//   'user uSeR4', 'user lastUser', 'uSeR4 posts on Books: I like books, I do really like them',
//   'uSeR4 posts on Movies: I also like movies, I really do', 'someUser posts on Shopping: title, I go shopping every day',
//  'someUser posts on Movies: Like, I also like movies very much']);

listUserComments(['user Mark',
 'Mark posts on someArticle: NoTitle, stupidComment',
  'article Bobby', 'article Steven', 'user Liam', 'user Henry',
   'Mark posts on Bobby: Is, I do really like them',
    'Mark posts on Steven: title, Run', 'someUser posts on Movies: Like']);