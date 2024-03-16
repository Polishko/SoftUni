function toggle() {
    let toggleStatus = document.getElementsByClassName('button')[0].textContent;
    
    if (toggleStatus === 'More') {
        document.getElementsByClassName('button')[0].textContent = 'Less';
        document.getElementById('extra').style.display = 'block';
    } else {
        document.getElementsByClassName('button')[0].textContent = 'More';
        document.getElementById('extra').style.display = 'none';
    }
    // console.log('TODO:...');
}