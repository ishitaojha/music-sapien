const quiz = [
    {
        "question": "Do you believe in Hardwork or Smartwork",
        "answers": [
            "Believe in Hardwork",
            "Believe in Smartwork",
        ],
    },
    {
        "question": "Did you prefer partying or listen to music while reading a book?",
        "answers": [
            "Partying",
            "Listen to music while reading a book",
        ],
    },
    {
        "question": "Do you love adventure ?",
        "answers": [
            "Yes",
            "No",
        ],
    }
]

const question = document.querySelector('.questions');
const option1 = document.querySelector('#option1');
const option2 = document.querySelector('#option2');
const option3 = document.querySelector('#option3');
const option4 = document.querySelector('#option4');

const answer = document.querySelectorAll('.answer');
const submit = document.querySelector('#submit');

const innerd = document.querySelector('.inner-div');

let count = 0;
var finalanswer = [];

const getQuestion = () => {
    let quizc = quiz[count];
    question.innerHTML = quizc.question;
    option1.innerHTML = quizc.answers[0];
    option2.innerHTML = quizc.answers[1];
    option3.innerHTML = quizc.answers[2];
    option4.innerHTML = quizc.answers[3];
}

const getSelected = () => {
    let ans;
    answer.forEach((curr) => {
        if (curr.checked) {
            ans = curr.id;
        }
    });
    if (ans == "ans1") {
        return option1.innerHTML;
    }
    if (ans == "ans2") {
        return option2.innerHTML;
    }
    if (ans == "ans3") {
        return option3.innerHTML;
    }
    return option4.innerHTML;

}
const defaultradio = () => {
    answer.forEach((curr) => { curr.checked = false });
}

submit.addEventListener('click', () => {
    const answer = getSelected();
    console.log(answer);
    count++;
    finalanswer.push(answer);
    if (count < quiz.length) {
        getQuestion();
    }
    else {
        innerd.innerHTML = `
   <h1>ThankYou</h1>
    <h3>Wait for 5 seconds</h3>
    `;
        $.ajax({
            type: "POST",
            url: "/get_answers",
            contentType: "application/json",
            data: JSON.stringify({"answers":finalanswer}),
            dataType: "json",
            success: function(response) {
                console.log(response);
            },
            error: function(err) {
                console.log(err);
            }
        });
        window.location.href="../song";
    }
    defaultradio();
});

getQuestion();
defaultradio();