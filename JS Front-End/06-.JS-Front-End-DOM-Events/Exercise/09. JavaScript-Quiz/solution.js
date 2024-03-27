function solve() {
  const answerIndexes = new Map([
    [0, 0],
    [1, 1],
    [2, 0],
  ]);

  const allLi = document.querySelectorAll('section li');
  const allSections = document.querySelectorAll('section');
  let correctAnswers = 0;
  
  Array.from(allLi).forEach((li) => {
    li.addEventListener('click', function(e) {
      const section = li.parentElement.parentElement; //Judge doesnt accept .closest()
      const sectionIndex = Array.from(allSections).indexOf(section);
      const sectionLi = section.querySelectorAll('.quiz-answer');
      const liIndex = Array.from(sectionLi).indexOf(li); 

      if (answerIndexes.get(sectionIndex) === liIndex) {
        correctAnswers += 1;
      }

      section.style.display = 'none';

      if (sectionIndex < 2) {
        const nextSection = allSections[sectionIndex + 1];
        nextSection.classList.remove('hidden');
        nextSection.style.display = 'block';
      } else {
        const resultUl = document.querySelector('#quizzie #results');
        resultUl.style.display = 'block';
        const result = document.querySelector('#results h1');
        result.textContent = (correctAnswers === 3) ? 'You are recognized as top JavaScript fan!' : `You have ${correctAnswers} right answers`;
      }
    });
  });
}
