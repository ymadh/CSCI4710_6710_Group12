
function score_quiz() {

    var vampireScore = 0;
    var quiz = document.getElementById("quiz");
    var error = document.getElementById("error");

    if (validate_form() === false) {
        error.style.display = "block";
        error.innerHTML = 'Please fill out the entire form';
        return;

    } else {
        error.innerHTML = '';
        error.style.display = "none";

    }

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


    var name = document.getElementById('firstName').value + ' ' + document.getElementById('lastName').value;
    if (vampireScore > 6) {
        document.getElementById("results").innerHTML = name + " is a Vampire!"
        drawChart('v');
    } else {
        document.getElementById("results").innerHTML = name + " is not a Vampire!"
        drawChart('h');
    }

}

function validate_form() {
    if (document.getElementById('firstName').value.length === 0) return false;
    if (document.getElementById('lastName').value.length === 0) return false;
    if (!document.getElementById("garlicRadio1").checked && !document.getElementById("garlicRadio2").checked) return false;
    if (!document.getElementById("complexionRadio1").checked && !document.getElementById("complexionRadio2").checked) return false;
    if (!document.getElementById("shadowRadio1").checked && !document.getElementById("shadowRadio2").checked) return false;
    if (!document.getElementById("iconOptions1").checked && !document.getElementById("iconOptions2").checked) return false;

    return true;
}
function headsOrTails() {
    var x = 0;
    var quiz = document.getElementById("quiz");
    quiz.style.display = "none";
    var results = document.getElementById("results");
    results.style.display = "block";

    x = Math.floor(Math.random() * 2);
    if (x == 0) {
        document.getElementById("results").innerHTML = "You are a Vampire!"
        drawChart('v');
    } else {
        document.getElementById("results").innerHTML = "You are not a Vampire!"
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