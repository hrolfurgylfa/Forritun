let nafnJSON = 'spurningar.json';
let spurningar;
let timi = 0;
let stig = 0;

//Sækja tengla úr HTML
timaTexti = document.getElementById("timi");
stigaTexti = document.getElementById("stig");

// ----- Sækja JSON skránna -----
fetch(nafnJSON)// Hérna er sótt JSON skránna
    .then(res => res.json())// Hérna er ... og það er notað .then til þess að það sé beðið eftir að það sé búið að sækja JSON skránna
    .then((out) => {
        spurningar = out;// Hérna er 
    });

setInterval(() => {
    timi++;
    timaTexti.textContent = timi;
},1000)

