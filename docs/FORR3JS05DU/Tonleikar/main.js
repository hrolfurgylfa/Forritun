"use strict";

// ----- Breytur -----
const nafnJSON = 'https://apis.is/concerts';
moment.locale("is");// Þetta breytir moment.js í íslensku

//Sækja tengla úr HTML og ég nota const vegna þess að þetta er eitthvað sem verður aldrei breytt
const geymslaAllraTonleikaMynda = document.getElementById("tonleikar");
const hladaTexti = document.getElementById("hladaTexti");
const searchBtn = document.getElementById("searchBtn");
const eftirDagsetningu  = document.getElementById("eftirDagsetningu");
const fyrirDagsetningu = document.getElementById("fyrirDagsetningu");
const leitarSlá = document.getElementById("leitarSlá");

// ----- Föll -----
let eftirJSONSótt = AllirTonleikar => {// Þetta er keyrt eftir að JSON skráin er sótt
    hladaTexti.remove();// Þetta eyðir textanum sem segir hleður... á meðan það er verið að sækja JSON skránna

    AllirTonleikar.forEach(tonleikar => {// Þetta keyrir í gegnum alla tónleikanna í JSON skránni og býr til hlut á DOM-ið fyrir hvern og einn
        geraTonleika(tonleikar);
    });

    // Hérna eru takkarnir búnir til vegna þess að það ef maður ýtir á takkana of snemma þá væri annars hægt að reyna að nota JSON skránna áður en hún er sótt
    searchBtn.addEventListener("click", evt => search(evt.target.previousElementSibling.value.toLowerCase(), AllirTonleikar), false);
    leitarSlá.addEventListener("change", evt => search(evt.target.value.toLowerCase(), AllirTonleikar), false);
    eftirDagsetningu.addEventListener("change", evt => tímaLeit(evt, AllirTonleikar), false);
    fyrirDagsetningu.addEventListener("change", evt => tímaLeit(evt, AllirTonleikar), false);
}
let geraTonleika = tonleikar => {// Þetta fall býr til tónleika á DOM-inu
    // Búa til myndacontainerinn
    let myndacontainer = buaTilElement("div");
    myndacontainer.classList.add("imageContainer");// Bæta klasa á myndacontainerinn
    
    // Búa til myndina
    let mynd = buaTilElement("img");
    mynd.src = tonleikar.imageSource;// Bæta link á myndina
    mynd.alt = "Mynd af tónleikunum "+tonleikar.eventDateName;// Bæta texta á myndina sem kemur ef myndin sést ekki
    mynd.classList.add("mynd");// Bæta klasa á myndina
    mynd.onload = function() { myndacontainer.classList.add("svartur_bakgrunnur"); }// Bæta klasa á mynacontainerinn þegar það er búið að hlatða myndinni vegna þess að annars kemur svartur bakgrunnur áður en myndin kemur yfir bakgrunninn
    myndacontainer.appendChild(mynd);// Þetta bætir myndinni við myndacontainerinn

    // Búa til texta containerinn
    let texti = buaTilElement("div");
    texti.classList.add("texti");// Bæta klasa á textann
    myndacontainer.appendChild(texti);// Þetta bætir textanum við myndacontainerinn
    
    // Búa til allann textan yfir myndunum
    buaTilElement("h3", tonleikar.eventDateName, texti, ["eventDateName"]);// Búa til fyrirsognina
    buaTilElement("h4", tonleikar.name, texti, ["name"]);// Búa til undirfyrirsongnina
    buaTilElement("p", tonleikar.eventHallName, texti, ["eventHallName"]);// Búa til staðsetninguna
    buaTilElement("p", moment(tonleikar.dateOfShow, "YYYY-MM-DDTHH:mm:ss").fromNow(), texti, ["timeUntilShow"]);// Búa til countdown tímann
    let timeStamp = tonleikar.dateOfShow.slice(8,10)+"."+tonleikar.dateOfShow.slice(5,7)+"."+tonleikar.dateOfShow.slice(0,4)+" "+tonleikar.dateOfShow.slice(11,13)+":"+tonleikar.dateOfShow.slice(14,16);// Búa til nákvæma tímann
    buaTilElement("p", timeStamp, texti, ["dateOfShow"]);// Bæta nákvæmnri dagsetningu við textann

    geymslaAllraTonleikaMynda.appendChild(myndacontainer);// Bæta mynda containerinnum við HTML skjalið
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
let search = (searchString, AllirTonleikar) => {// Þetta fall leitar í tónleikunum og tékkar hvort að searchString sé eitthverstaðar í tónleikunum
    eyðaÖllumBörnum(geymslaAllraTonleikaMynda);

    // Hreinsa dagsetningar vegna þess að þær virka ekki með leitinni
    eftirDagsetningu.value = "";
    fyrirDagsetningu.value = "";

    AllirTonleikar.forEach(tonleikar => {// Þetta keyrir í gegnum alla tónleikanna og tékkar hvort að það sem var leitað að hafi verið eitthverstaðar, ef það er eitthverstaðar þá er búið til tónleikanna
        if (tonleikar.eventDateName.toLowerCase().includes(searchString) || tonleikar.name.toLowerCase().includes(searchString) || tonleikar.userGroupName.toLowerCase().includes(searchString) || tonleikar.eventHallName.toLowerCase().includes(searchString)) {// Þetta tékkar hvort að leitarstrengurinn sé eitthverstaðar í tónleikunum
            geraTonleika(tonleikar);
        }
    });
}
let tímaLeit = (evt, AllirTonleikar) => {// Þetta fall tekur báðar dagsetningarnar(eða bara eina) og finnur alla tónleika á milli þessara dagsetninga (eða ef það er bara ein þá er fundið annaðhvort fyrir eða eftir dagsetninguna)
    eyðaÖllumBörnum(geymslaAllraTonleikaMynda);

    leitarSlá.value = "";// Hreinsa leitarslá vegna þess að hún virkar ekki með dagsetningunni

    if (eftirDagsetningu.value != "" && fyrirDagsetningu.value != "") {// Finna tónleika á milli dagsetninga
        // Hérna bý ég til Date object fyrir báðar dagsetningarnar til þess að geta svo borið þær við dagsetningu hverra tónleika
        let eftirDagsetninguDate = new Date(eftirDagsetningu.value.slice(0,4), eftirDagsetningu.value.slice(5,7), eftirDagsetningu.value.slice(8,10));
        let fyrirDagsetninguDate = new Date(fyrirDagsetningu.value.slice(0,4), fyrirDagsetningu.value.slice(5,7), fyrirDagsetningu.value.slice(8,10));

        AllirTonleikar.forEach(tonleikar => {// Þetta keyrir í gegnum alla tónleikana og tékkar hvort að þeir séu á milli dagsetningana sem voru búnar til
            let tonleikaDagsetning = new Date(tonleikar.dateOfShow.slice(0,4), tonleikar.dateOfShow.slice(5,7), tonleikar.dateOfShow.slice(8,10));// Hérna bý ég til Date object fyrir tónleikanna sem er verið að keyra í gegnum til þess að það sé svo hægt að bera þá saman við hina Date objectana
            if (tonleikaDagsetning >= eftirDagsetninguDate && tonleikaDagsetning <= fyrirDagsetninguDate) {// Þetta býr til tónleikanna ef þeir eru á milli date objectanna
                geraTonleika(tonleikar);
            }
        });
    } else if (eftirDagsetningu.value != "" && fyrirDagsetningu.value === "") {// Finna tónleika eftir dagsetningu
        // Hérna bý ég til Date object fyrir eina dagsetninguna til þess að geta svo borið hana við dagsetningu hverra tónleika
        let eftirDagsetninguDate = new Date(eftirDagsetningu.value.slice(0,4), eftirDagsetningu.value.slice(5,7), eftirDagsetningu.value.slice(8,10));

        AllirTonleikar.forEach(tonleikar => {// Þetta keyrir í gegnum alla tónleikana og tékkar hvort að þeir séu á eftir dagsetningunni sem vor búin til
            let tonleikaDagsetning = new Date(tonleikar.dateOfShow.slice(0,4), tonleikar.dateOfShow.slice(5,7), tonleikar.dateOfShow.slice(8,10));// Hérna bý ég til Date object fyrir tónleikanna sem er verið að keyra í gegnum til þess að það sé svo hægt að bera þá saman við hina Date objectana
            if (tonleikaDagsetning >= eftirDagsetninguDate) {// Þetta býr til tónleikanna ef þeir eru eftir date objectinn sem var búinn til
                geraTonleika(tonleikar);
            }
        });
    } else if (eftirDagsetningu.value === "" && fyrirDagsetningu.value != "") {// Finna tónleika fyrir dagsetningu
        // Hérna bý ég til Date object fyrir eina dagsetninguna til þess að geta svo borið hana við dagsetningu hverra tónleika
        let fyrirDagsetninguDate = new Date(fyrirDagsetningu.value.slice(0,4), fyrirDagsetningu.value.slice(5,7), fyrirDagsetningu.value.slice(8,10));
        
        AllirTonleikar.forEach(tonleikar => {// Þetta keyrir í gegnum alla tónleikana og tékkar hvort að þeir séu á fyrir dagsetninguna sem var búin til
            let tonleikaDagsetning = new Date(tonleikar.dateOfShow.slice(0,4), tonleikar.dateOfShow.slice(5,7), tonleikar.dateOfShow.slice(8,10));// Hérna bý ég til Date object fyrir tónleikanna sem er verið að keyra í gegnum til þess að það sé svo hægt að bera þá saman við hina Date objectana
            if (tonleikaDagsetning <= fyrirDagsetninguDate) {// Þetta býr til tónleikanna ef þeir eru fyrir date objectinn sem var búinn til
                geraTonleika(tonleikar);
            }
        });
    } else {// Það er búið að hreinsa bæði hólfin svo að ég sýni allt
        AllirTonleikar.forEach(tonleikar => {// Þetta keyrir í gegnum alla tónleikanna og búr þá til á HTML skjalinu
            geraTonleika(tonleikar);
        });
    }
}
let eyðaÖllumBörnum = foreldri => {// Þetta fall eyðir öllum börnum elementsins sem er sendur inn
    while (foreldri.firstChild) {// Þetta keyrir þangað til það eru engin börn
        foreldri.firstChild.remove();// Þetta eyðir fyrsta barninu
    }
}

// Hreinsa dagsetninga og leitar valið vegna þess að ef það er refreshað þá er ekki leitað þótt að inputið haldist í sumum vöfrum
eftirDagsetningu.value = "";
fyrirDagsetningu.value = "";
leitarSlá.value = "";

// ----- Sækja JSON skránna -----
fetch(nafnJSON)// Hérna er sótt JSON skránna
    .then(res => res.json())// Hérna er breytt því sem var sótt í Object fyrir JavaScript og það er notað .then til þess að það sé biðið eftir að það sé búið að sækja JSON skránna
    .then(out => eftirJSONSótt(out.results));// Hérna er objectinn sendur í fallið eftirJSONSótt þar sem allur kóðinn er sem á að keyra eftir að JSON skráin er sótt
