function focused() {
    let inputAreas = Array.from(document.querySelectorAll('input')); //Convert to Array for Judge tests

    inputAreas.forEach(element => element.addEventListener('focus', highlight));
    inputAreas.forEach(element => element.addEventListener('blur', removeHighlight));

    function highlight(e) {
        const target = e.currentTarget.parentNode;
        target.classList.add('focused');
    }

    function removeHighlight(e) {
        const target = e.currentTarget.parentNode;
        target.classList.remove('focused');
    }
}