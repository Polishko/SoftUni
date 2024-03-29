function attachEvents() {
    POSTS_URL = 'http://localhost:3030/jsonstore/blog/posts';
    COMMENTS_URL = 'http://localhost:3030/jsonstore/blog/comments';

    const loadButton = document.getElementById('btnLoadPosts');
    const viewButton = document.getElementById('btnViewPost');

    const selectItem = document.getElementById('posts');
    const titleElement = document.getElementById('post-title');
    const bodyElement = document.getElementById('post-body');
    const ulElement = document.getElementById('post-comments');

    let allPosts;

    const loadPosts = function() {
        selectItem.innerHTML = '';

        fetch(POSTS_URL)
        .then((response) => response.json())
        .then((data) => {
            allPosts = Object.entries(data);
                     
            for (obj of allPosts) {
                const option = document.createElement('option');
                option.value = obj[1].id; // Mistake in problem explanation: it says use object key or obj[0]
                option.textContent = obj[1].title;
                selectItem.add(option);
            }
        })
        .catch((error) => error)
    };

    const viewComments = function() {
        const postObj = allPosts.find((post) => selectItem.value === post[1].id);
        const idPost = postObj[1].id;
        titleElement.textContent = postObj[1].title;
        bodyElement.textContent = postObj[1].body;
        
        fetch(COMMENTS_URL)
        .then((response) => response.json())
        .then((data) => {
            const commentsArray = Object.entries(data);
            const filteredComments = commentsArray.filter((obj) => obj[1].postId === idPost);
            
            ulElement.innerHTML = '';
            for (comment of filteredComments) {
                const liElement = document.createElement('li');
                liElement.textContent = comment[1].text;
                ulElement.appendChild(liElement);
            }
        })
        .catch((error) => error)
    };

    loadButton.addEventListener('click', loadPosts);
    viewButton.addEventListener('click', viewComments);

}

attachEvents();