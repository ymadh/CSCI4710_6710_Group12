
function score_quiz() {

    var vampireScore = 0;
    var quiz = document.getElementById("quiz");
    quiz.style.display = "none";
    var results = document.getElementById("results");
    results.style.display = "block";

    // default case
    var icon = 'human.png';
    if (document.getElementById('iconOptions1').checked) {
        icon = 'vampire.jpg';
    }
    if (document.getElementById('iconOptions2').checked) {
        icon = 'human.png';
    }

    if (document.getElementById('shadowRadio2').checked) {
        vampireScore += 4;
    };

    if (document.getElementById('complexionRadio1').checked) {
        vampireScore += 3;
    }

    if (document.getElementById('garlicRadio1').checked) {
        vampireScore += 3;
    }

    console.log(vampireScore);
    return (vampireScore > 6);
}