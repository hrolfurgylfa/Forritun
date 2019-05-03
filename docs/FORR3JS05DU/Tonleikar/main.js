"use strict";

// ----- Breytur -----
const nafnJSON = 'https://apis.is/concerts';
moment.locale("is");// Þetta breytir moment.js í íslensku

//Sækja tengla úr HTML og ég nota const vegna þess að þetta er eitthvað sem verður aldrei breytt
const geymslaAllraTonleikaMynda = document.getElementById("tonleikar");
const hladaTexti = document.getElementById("hladaTexti");
const searchBtn = document.getElementById("searchBtn");

// ----- Föll -----
let eftirJSONSótt = AllirTonleikar => {
    hladaTexti.remove();

    AllirTonleikar.forEach(tonleikar => {
        geraTonleika(tonleikar);
    });

    searchBtn.addEventListener("click", evt => search(evt, AllirTonleikar), false);
}
let geraTonleika = tonleikar => {
    // Búa til myndacontainerinn
    let myndacontainer = document.createElement("div");
    myndacontainer.classList.add("imageContainer");
    
    // Búa til myndina
    let mynd = document.createElement("img");
    mynd.src = tonleikar.imageSource;
    mynd.alt = "Mynd af tónleikunum "+tonleikar.eventDateName;
    mynd.classList.add("mynd");
    mynd.onload = function() { myndacontainer.classList.add("svartur_bakgrunnur"); }
    myndacontainer.appendChild(mynd);

    // Búa til texta containerinn
    let texti = buaTilElement("div");
    texti.classList.add("texti");
    myndacontainer.appendChild(texti);
    
    // Búa til allann textan yfir myndunum
    buaTilElement("h3", tonleikar.eventDateName, texti, ["eventDateName"]);// Búa til fyrirsognina
    buaTilElement("h4", tonleikar.name, texti, ["name"]);// Búa til undirfyrirsongnina
    buaTilElement("p", tonleikar.eventHallName, texti, ["eventHallName"]);// Búa til staðsetninguna
    buaTilElement("p", moment(tonleikar.dateOfShow, "YYYY-MM-DDTHH:mm:ss").fromNow(), texti, ["timeUntilShow"]);// Búa til countdown
    let timeStamp = tonleikar.dateOfShow.slice(8,10)+"."+tonleikar.dateOfShow.slice(5,7)+"."+tonleikar.dateOfShow.slice(0,4)+" "+tonleikar.dateOfShow.slice(11,13)+":"+tonleikar.dateOfShow.slice(14,16);
    buaTilElement("p", timeStamp, texti, ["dateOfShow"]);// Búa til nákvæma dagsetningu

    geymslaAllraTonleikaMynda.appendChild(myndacontainer);
}
let buaTilElement = (element, texti = false, foreldri = false, classList = false) => {// Þetta fall býr til element en það þarf ekki endilega að senda inn neitt nema hvernig hlut þér langar í
    let item = document.createElement(element);// hérna er hluturinn búinn til

    if (texti !== false) {// Þetta keyrir ef það var sendur texti með
        let texta_element = document.createTextNode(texti);// Hérna er textinn búin til
        item.appendChild(texta_element);// Hérna er bætt textanum undir hlutin sem er verið að búa til
    }
    if (classList !== false) {// Þetta bætir við öllum klösunum í arrayingum classlist (ef hann er sendur inn)
        classList.forEach(className => item.classList.add(className));
    }
    if (foreldri !== false) {// Þetta keyrir ef það var sent foreldri með
        foreldri.appendChild(item);// Hérna er bætt hlutnum við foreldrið sem var sent inn
    } else {
        return item;// Hérna er skilað hlutnum ef það var ekki send neitt foreldri með
    }
}
let search = (evt, AllirTonleikar) => {
    while (geymslaAllraTonleikaMynda.firstChild) {// Þetta keyrir þangað til það eru engin börn
        geymslaAllraTonleikaMynda.firstChild.remove();// Þetta eyðir fyrsta barninu
    }

    let searchString = evt.target.previousElementSibling.textContent;
    console.log(searchString);

    AllirTonleikar.forEach(tonleikar => {
        console.log(searchString.search(tonleikar.eventDateName));

        if (searchString.search(tonleikar.eventDateName) != -1) {
            console.log("Found");
            geraTonleika(tonleikar);
        }
    });
}

// ----- Sækja JSON skránna -----
fetch(nafnJSON)// Hérna er sótt JSON skránna
    .then(res => res.json())// Hérna er breytt því sem var sótt í Object fyrir JavaScript og það er notað .then til þess að það sé biðið eftir að það sé búið að sækja JSON skránna
    .then(out => eftirJSONSótt(out.results));// Hérna er objectinn sendur í fallið eftirJSONSótt þar sem allur kóðinn er sem á að keyra eftir að JSON skráin er sótt