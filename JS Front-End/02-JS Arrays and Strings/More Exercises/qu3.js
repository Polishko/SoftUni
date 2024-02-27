function buildPyramid(width, increment) {
    let stones = 0, marble = 0, lapis = 0, gold = 0;
    let lowestStep = width % 2 !== 0 ? 1 : 2;
    let height = Math.floor(((width - lowestStep) / 2 + 1) * increment);
    let steps = 0;

    for (let i = width; i >= lowestStep; i -= 2) {
        steps += 1;

        if (i === lowestStep) {
            gold = (lowestStep ** 2) * increment;
            break;
        }

        outer = (((i - 2) * 4 + 4) * increment);
        stones += (((i - 2) ** 2) * increment);
        steps % 5 === 0 ? lapis += outer : marble += outer;
    }

    console.log(`Stone required: ${Math.ceil(stones)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${height}`);
}


// buildPyramid(11, 1);
// buildPyramid(11, 0.75);
// buildPyramid(12, 1);
// buildPyramid(23, 0.5);
