
function score_quiz() {

    var vampireScore = 0;
    var quiz = document.getElementById("quiz");
    quiz.style.display = "none";
    var results = document.getElementById("results");
    results.style.display = "block";

    // default case
    var icon = "human.png";
    if (document.getElementById("iconOptions1").checked) {
        icon = "vampire.jpg";
    }
    if (document.getElementById("iconOptions2").checked) {
        icon = "human.png";
    }

    if (document.getElementById("shadowRadio2").checked) {
        vampireScore += 4;
    };

    if (document.getElementById("complexionRadio1").checked) {
        vampireScore += 3;
    }

    if (document.getElementById("garlicRadio1").checked) {
        vampireScore += 3;
    }

    console.log(vampireScore);
    if (vampireScore > 6) {
        document.getElementById("results").innerHTML = "is a Vampire!"
    } else {
        document.getElementById("results").innerHTML = "is not a Vampire!"
    }

}

function headsOrTails() {
    var randomVampireScore = 0;
    var quiz = document.getElementById("quiz");
    quiz.style.display = "none";
    var results = document.getElementById("results");
    results.style.display = "block";

    randomVampireScore = Math.floor(Math.random() * Math.floor(max))
    if (vampireScore == 1) {
        document.getElementById("results").innerHTML = "is a Vampire!"
    } else {
        document.getElementById("results").innerHTML = "is not a Vampire!"
    }
}