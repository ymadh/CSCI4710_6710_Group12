
function score_quiz() {
    console.log('Score the quiz!');
    var quiz = document.getElementById("quiz");
    quiz.style.display = "none";
    var results = document.getElementById("results");
    results.style.display = "block";

    if (document.getElementById('shadowRadio1').checked) {
        var shadow = 0
    } else if (document.getElementById('shadowRadio2').checked) {
        var shadow = 4
    };

    if (document.getElementById('complexionRadio1').checked) {
        var complexion = 3
    } else if (document.getElementById('complexionRadio2').checked) {
        var complexion = 0
    };

    if (document.getElementById('garlicRadio1').checked) {
        var garlic = 3
    } else if (document.getElementById('garlicRadio2').checked) {
        var garlic = 0
    };

    switch (true) {
        case (shadow + complexion + garlic) > 6:
            vampire = true;
            return vampire;
            break;
        case (shadow + complexion + garlic) <= 6:
            vampire = false;
            return vampire;
            break;
    }
}