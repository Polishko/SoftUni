function attachEvents() {
    const URL = 'http://localhost:3030/jsonstore/messenger';
    const sendButton = document.getElementById('submit');
    const refreshButton = document.getElementById('refresh');
    let postMessage;
    
    const sendMessage = function() {
        const author = document.querySelector('input[name="author"]');
        const content = document.querySelector('input[name="content"]');

        postMessage = {
            'author': author.value,
            'content': content.value,
        };

        fetch(`${URL}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postMessage)
        })
        .catch((error) => console.log(error.message))

        author.value = '';
        content.value = '';
    };

    const refreshMessage = function() {
        const textElement = document.getElementById('messages');
        let result = [];

        fetch(`${URL}`)
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            for (const messageObj of Object.entries(data)) {
                const messageAuthor = messageObj[1].author;
                const messageContent = messageObj[1].content;
                result.push(`${messageAuthor}: ${messageContent}`);
            }
        textElement.value = result.join('\n');
        })
        .catch((error) => error);
    };

    sendButton.addEventListener('click', sendMessage);
    refreshButton.addEventListener('click', refreshMessage);
}

attachEvents();