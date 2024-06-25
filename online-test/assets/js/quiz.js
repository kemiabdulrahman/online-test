console.log("hello world");

const url = window.location.href
console.log(url);

quizBox = document.getElementById('quiz-box')
let data


$.ajax({
  type: 'GET',
  url: `${url}data`,

  success: function(response) {
   console.log(response); 
    const data = response.data
    data.forEach(el => {
    for ( const [question, answers] of Object.entries(el))
      {
        quizBox.innerHTML += `
              <hr>
              <div class="form-group">
              <b>
                    <label class="font-weight-bold">${question}</label>
              </b>
                    `
        answers.forEach(answer => {
          quizBox.innerHTML += 

                    `
                    <div class="form-check">
                        <input id="${question}-${answer}" class="form-check-input ans" type="radio" name="${question}" value=${answer}>
                        <label class="form-check-label" for="${question}">${answer}</label>
                    </div>
              </div>
        `
        });
        console.log(question);
        console.log(answers);
      } 
    });
  },

  error: function(error) {
   console.log(error); 
  }

})

const quizForm = $('#quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const sendData = () => {
  const elements = [...$('.ans')]
  const data = {}
  data['csrfmiddlewaretoken'] = csrf[0].value
  elements.forEach(el => {
    if (el.checked) {
      data[el.name] = el.value 
      
    } else {
      if (!data[el.name]) {
        data[el.name] = null
      }
    }
  })

  $.ajax({
    type: 'POST',
    url: `${url}save/`,
    data: data,

    success: function(response) {
      console.log(response);
    },

    error: function(error) {
     console.log(error); 
    }
    })
}

quizForm.on('submit', (e) => {
  e.preventDefault();

  sendData()
})

