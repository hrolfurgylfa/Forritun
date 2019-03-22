"use strict";

// ----- Viðbætt föll á algenga objects -----
Array.prototype.shuffle = function() {
    for (let i = this.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [this[i], this[j]] = [this[j], this[i]];
    }
}

// ----- Breytur -----
const nafnJSON = 'spurningar.json';
let spurningar = [];
let timi = 0;
let stig = 0;
let spurningarNumer = 1;
let rettSvor = 0;
let rongSvor = 0;

//Sækja tengla úr HTML
const spurningarTexti = document.getElementById("spurning");
const spurningarNumerTexti = document.getElementById("numerSpurningar");
const fjoldiSpurningaTexti = document.getElementById("fjoldiSpurninga");
const timaTexti = document.getElementById("timi");
const rettraSvaraTexti = document.getElementById("rettSvor");
const rangraSvaraTexti = document.getElementById("rongSvor");
const svaraStadur = document.getElementById("svor");
const spilaAftur = document.getElementById("spila_aftur");
const spilaAfturTakki = document.getElementById("spila_aftur_mynd");

// ----- Föll -----
let tengtJSON = () => {
    // Texta sem breytist aldrei breytt
    fjoldiSpurningaTexti.textContent = spurningar.length;

    setjaUppSpurningu(spurningar[spurningarNumer-1]);
}
let setjaUppSpurningu = (spurning) => {
    // Hreinsa allt í burtu
    while (svaraStadur.firstChild) {
        svaraStadur.firstChild.remove();
    }

    // Texta sem breytist við hverja spurningu breytt
    spurningarTexti.textContent = spurning.Spurning;
    spurningarNumerTexti.textContent = spurningarNumer;

    // Búa til takka
    let svarNumer = 1;
    spurning.Svar = Number(spurning.Svar);
    spurning.Svor.forEach(svar => {
        if (svarNumer != spurning.Svar) {
            buaTilSvarmoguleika(svar, svarNumer, spurning.Eining, false);
        } else {
            buaTilSvarmoguleika(svar, svarNumer, spurning.Eining, true);
        }
        svarNumer++;
    });
}
let buaTilSvarmoguleika = (svar, numer, eining, erRett) => {
    let nyrTakki = document.createElement("div"); 
    let nyrTexti = document.createTextNode(svar + eining);

    nyrTakki.appendChild(nyrTexti);
    nyrTakki.classList.add("svar"+numer);

    if (erRett === false) {nyrTakki.addEventListener("click",rangtSvar,false)}
    else {nyrTakki.addEventListener("click",rettSvar,false);}

    svaraStadur.appendChild(nyrTakki);
}
let rettSvar = (evt) => {
    rettSvor ++;
    rettraSvaraTexti.textContent = rettSvor;
    evt.target.style.backgroundColor = "rgb(0,255,0)";
    
    if (spurningarNumer != spurningar.length) {
        spurningarNumer++;
        setjaUppSpurningu(spurningar[spurningarNumer-1]);
    } else {// Hérna er Quizið búið
        clearInterval(skeidklukka);

        let born = Array.from(svaraStadur.children);
        born.forEach(barn => {
            barn.removeEventListener("click",rangtSvar,false);
            barn.removeEventListener("click",rettSvar,false);
        });

        spilaAftur.classList.remove("falid");
    }
}
let rangtSvar = (evt) => {
    rongSvor ++;
    rangraSvaraTexti.textContent = rongSvor;
    evt.target.style.backgroundColor = "rgb(255,0,0)";
}

// ----- Sækja JSON skránna -----
fetch(nafnJSON)// Hérna er sótt JSON skránna
    .then(res => res.json())// Hérna er ... og það er notað .then til þess að það sé beðið eftir að það sé búið að sækja JSON skránna
    .then(out => {
        out.shuffle();
        out.forEach(spurning => {
            spurningar.push(spurning);
        });
        tengtJSON();
    });

// Gera tagsetningu tilbúna fyrir timerinn
let byrjunarDagsetning = new Date().getTime();

// Timer sem keyrir 10 sinnum á sekúndu til þess að timerinn sé allveg réttur
let skeidklukka = setInterval(() => {
    timi = new Date().getTime() - byrjunarDagsetning;
    timaTexti.textContent = Math.floor(timi/1000);
},100);

spilaAfturTakki.addEventListener("click",() => {location.reload();},false);