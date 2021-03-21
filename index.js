
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
        drawChart('v');
    } else {
        document.getElementById("results").innerHTML = "is not a Vampire!"
        drawChart('h');
    }

}

function headsOrTails() {
    var randomVampireScore = 0;
    var quiz = document.getElementById("quiz");
    quiz.style.display = "none";
    var results = document.getElementById("results");
    results.style.display = "block";

    randomVampireScore = Math.floor(Math.random() * Math.floor(max))
    if (randomVampireScore == 1) {
        document.getElementById("results").innerHTML = "is a Vampire!"
        drawChart('v');
    } else {
        document.getElementById("results").innerHTML = "is not a Vampire!"
        drawChart('h');
    }
}
//Google Charts Code:

//setup for chart
google.charts.load('current', { 'packages': ['corechart'] });
//google.charts.setOnLoadCallback(drawChart);
//Variables
var chart;
var data;
var options;
var humans = 15;
var vampires = 10;

function drawChart(augment) {

    if (augment == 'h') {
        humans += 1;
    } else {
        vampires += 1;
    }
    //create table
    data = new google.visualization.DataTable();
    data.addColumn('string', 'Element');
    data.addColumn('number', 'Number');
    data.addRows([
        ['Human', humans],
        ['Vampire', vampires]
    ]);

    options = {
        'title': 'Vampires in the class now:',
        'width': 500,
        'height': 400,
        'chartArea,left': 100
    };
    chart = new google.visualization.PieChart(document.getElementById('chart_div'));
    chart.draw(data, options);

}