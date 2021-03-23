var classmateData = [
    {
        'name': 'John',
        'shadow': 0,
        'galic': 0,
        'complexion': 1,
        'icon': 'h',
    },
    {
        'name': 'Lee',
        'shadow': 1,
        'galic': 1,
        'complexion': 1,
        'icon': 'v',
    },
    {
        'name': 'Emma',
        'shadow': 0,
        'galic': 1,
        'complexion': 0,
        'icon': 'h',
    },
    {
        'name': 'Ava',
        'shadow': 1,
        'galic': 1,
        'complexion': 0,
        'icon': 'h'
    },
    {
        'name': 'Alex',
        'shadow': 1,
        'galic': 1,
        'complexion': 1,
        'icon': 'v'
    },
];
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
    var newObj = {};
    newObj.shadow = 0;
    newObj.name = '';
    newObj.complexion = 0;
    newObj.garlic = 0;

    // default case
    var icon = "human.png";
    if (document.getElementById("iconOptions1").checked) {
        icon = "vampire.jpg";

    }
    if (document.getElementById("iconOptions2").checked) {
        icon = "human.png";
    }
    newObj.icon = icon;

    if (document.getElementById("shadowRadio2").checked) {
        vampireScore += 4;
        newObj.shadow = 1;
    };

    if (document.getElementById("complexion").value == 1) {

        vampireScore += 3;
        newObj.complexion = 1;
    }

    if (document.getElementById("garlicRadio1").checked) {
        vampireScore += 3;
        newObj.garlic = 1;
    }


    var name = document.getElementById('firstName').value + ' ' + document.getElementById('lastName').value;
    newObj.name = name;
    classmateData.push(newObj);
    insertRow(newObj);

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
    if (!document.getElementById("complexion").selectedIndex === -1) return false;
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

    var newObj = {};
    newObj.shadow = 0;
    newObj.name = '';
    newObj.complexion = 0;
    newObj.garlic = 0;

    for (const property in newObj) {
        let rand = Math.floor(Math.random() * 2);
        newObj.property = rand;
    }

    newObj.name = 'Random';

    insertRow(newObj);
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

render_table();

/**
 * initial render of the table
 */
function render_table() {

    for (let i = 0; i < classmateData.length; i++) {
        insertRow(classmateData[i]);
    }
}

/** 
 * create rows
 */
function insertRow(rowObj) {
    var table = document.getElementById("results_table");
    let row = table.insertRow(-1);

    let cell1 = row.insertCell(0);
    let cell2 = row.insertCell(1);
    let cell3 = row.insertCell(2);
    let cell4 = row.insertCell(3);
    let cell5 = row.insertCell(4);

    cell1.innerHTML = rowObj.name;
    cell2.innerHTML = rowObj.shadow ? 'Shadow' : 'No Shadow';
    cell3.innerHTML = rowObj.complexion ? 'Pale' : 'Not Pale';
    cell4.innerHTML = rowObj.garlic ? 'Love Garlic' : 'Hate Garlic';
    cell5.innerHTML = rowObj.icon === 'v' ? '<img src="vampire.jpg" width="50">' : '<img src="human.png" width="50">';

}
