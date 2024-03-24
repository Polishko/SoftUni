function validate() {
    let input = document.getElementById('email');

    input.addEventListener('change', validate);
    
    function validate(e) {
        let currentInput = input.value;
        const pattern = /^[a-z]+@[a-z]+\.[a-z]+$/;

        if (!pattern.test(currentInput)) {
            input.classList.add('error');
        } else {
            input.classList.remove('error');
        }
    }
}