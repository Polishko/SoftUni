function attachGradientEvents() {
    let gradient = document.getElementById('gradient');
    gradient.addEventListener('mousemove', gradientMove);
    gradient.addEventListener('mouseput', gradientOut);

    function gradientMove(event) {
        let gradientPower = event.offsetX / (event.target.clientWidth - 1); //why 1 and not 2? the border is 2px
        let percentPower = Math.floor(gradientPower * 100);
        document.getElementById('result').textContent = `${percentPower}%`;
    }

    function gradientOut(event) {
        document.getElementById('result').textContent = '';
    }
}