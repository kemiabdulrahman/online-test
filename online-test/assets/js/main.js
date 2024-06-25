console.log("hello world");

const modalBtns = [...$('.modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn  = document.getElementById('start-button')
const url = window.location.href

console.log(modalBody);

console.log(modalBtns);
modalBtns.forEach(modalBtn => {
  modalBtn.addEventListener('click', () => {
    console.log(modalBtn);
    const pk = modalBtn.getAttribute('data-bs-pk')
    console.log(pk);
    const name = modalBtn.getAttribute('data-bs-quiz')
    const numQuestions = modalBtn.getAttribute('data-bs-questions')
    const difficulty = modalBtn.getAttribute('data-bs-difficulty')
    const time = modalBtn.getAttribute('data-bs-time')


    modalBody.innerHTML = `

        <div>
          <div class="h5 mb-3">
            Are you sure you want to begin "<b>${name}</b>"?
          </div>
          <div class="text-muted">
            <ul>
              <li>difficulty: <b>${difficulty}</b></li>
              <li>number_of_questions: ${numQuestions}</li>
              <li>time: ${time}min</li>
            </ul>
          </div>
        </div>
    `

  startBtn.addEventListener('click', () => {
    console.log(window.location.href);
    window.location.href = url + pk
  })

  })
})

