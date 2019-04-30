"use strict";

// ----- Breytur -----
const nafnJSON = 'https://apis.is/concerts';

//Sækja tengla úr HTML og ég nota const vegna þess að þetta er eitthvað sem verður aldrei breytt
const geymslaAllraTonleikaMynda = document.getElementById("tonleikar");

// ----- Föll -----
let eftirJSONSótt = AllirTonleikar => {
    AllirTonleikar.forEach( tonleikar => {
        geraTonleika(tonleikar);
    });
}
let geraTonleika = tonleikar => {
    // Búa til myndacontainerinn
    let myndacontainer = document.createElement("div");
    myndacontainer.classList.add("imageContainer");
    myndacontainer.addEventListener("pointerenter", synaTexta, false);
    myndacontainer.addEventListener("pointerleave", felaTexta, false);
    
    // Búa til myndina
    let mynd = document.createElement("img");
    mynd.src = tonleikar.imageSource
    mynd.alt = "Mynd af tónleikunum "+tonleikar.eventDateName
    mynd.classList.add("mynd");
    myndacontainer.appendChild(mynd);

    // Búa til texta containerinn
    let texti = document.createElement("div");
    texti.classList.add("texti");
    myndacontainer.appendChild(texti);

    // Búa til fyrirsognina
    let fyrirsongn = document.createElement("h3");
    let fyrirsongn_texti = document.createTextNode(tonleikar.eventDateName);
    fyrirsongn.appendChild(fyrirsongn_texti);
    texti.appendChild(fyrirsongn);


    geymslaAllraTonleikaMynda.appendChild(myndacontainer);
}
let synaTexta = evt => {
    if (evt.pointerType == "mouse") {
        console.log(evt);
        
    }
}
let felaTexta = evt => {
    if (evt.pointerType == "mouse") {
        console.log(evt);
    }
}

// ----- Sækja JSON skránna -----
fetch(nafnJSON)// Hérna er sótt JSON skránna
    .then(res => res.json())// Hérna er breytt því sem var sótt í Object fyrir JavaScript og það er notað .then til þess að það sé biðið eftir að það sé búið að sækja JSON skránna
    .then(out => eftirJSONSótt(out.results));// Hérna er objectinn sendur í fallið eftirJSONSótt þar sem allur kóðinn er sem á að keyra eftir að JSON skráin er sótt