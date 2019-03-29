"use strict";

// ----- Viðbætt föll á algenga objects -----
Array.prototype.shuffle = function() {// Þetta bætir .shuffle() við alla lista og ef það er keyrt þá er ruglað listanum. Ég fékk þennan kóða af netinu en ég bætti honum við Arrey.prototype sjálfur
    for (let i = this.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [this[i], this[j]] = [this[j], this[i]];
    }
}

// ----- Breytur -----
const nafnJSON = 'spurningar.json';
let spurningar = [];
let timi = 0;
let spurningarNumer = 1;
let rettSvor = 0;
let rongSvor = 0;

//Sækja tengla úr HTML og ég nota const vegna þess að þetta er eitthvað sem verður aldrei breytt
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
let setjaUppSpurningu = (spurning) => {// Þetta fall setur upp nýja spurningu
    // Hreinsa allt í burtu
    while (svaraStadur.firstChild) {// Þetta keyrir þangað til það eru engin börn
        svaraStadur.firstChild.remove();// Þetta eyðir fyrsta barninu
    }

    // Texta breytt sem breytist við hverja spurningu
    spurningarTexti.textContent = spurning.Spurning;
    spurningarNumerTexti.textContent = spurningarNumer;

    // Búa til takka
    let svarNumer = 1;
    spurning.Svar = Number(spurning.Svar);// Þetta breytir breytuni sem geymir rétta svarið úr streng í heiltölu
    spurning.Svor.forEach(svar => {// Þetta keyrir í gegnum svörin og ef svarið sem kemur er rétta svarið sendir þetta þær upplýsingar með í buaTilSvarmoguleika fallið
        if (svarNumer != spurning.Svar) {
            buaTilSvarmoguleika(svar, svarNumer, spurning.Eining, false);
        }
        else {
            buaTilSvarmoguleika(svar, svarNumer, spurning.Eining, true);
        }
        svarNumer++;
    });
}
let buaTilSvarmoguleika = (svar, numer, eining, erRett) => {// Þetta bætir við einum svarmöguleika
    let nyrTakki = document.createElement("div"); // Þetta býr til <div> element en það er ekki komið neitt í HTMLinu heldur geymir það bara í breytu
    let nyrTexti = document.createTextNode(svar + eining);// Þetta býr til texta fyrir HTML element en þetta er bara geymt í breytu

    nyrTakki.appendChild(nyrTexti);// Hérna festi ég textann við <div> elementið
    nyrTakki.classList.add("svar"+numer);// Hérna bæti ég klasa við <div> elementið

    if (erRett === false) {nyrTakki.addEventListener("click",rangtSvar,false)}// Hérna bæti ég við eventListener ef svarið sem er verið að búa til er ekki rétt
    else {nyrTakki.addEventListener("click",rettSvar,false);}// Hérna bæti ég við eventListener ef svarið sem er verið að búa til er rétt

    svaraStadur.appendChild(nyrTakki);// Hérna bæti ég svarmöguleikanum við HTML skjalið undir því sem er með IDið svor
}
let rettSvar = (evt) => {// Þetta er keyrt ef það var ýtt á rétt svar
    rettSvor ++;
    rettraSvaraTexti.textContent = rettSvor;// Textinn uppfærður
    evt.target.style.backgroundColor = "rgb(0,255,0)";// Hérna er bakgrunnslitinum breytt
    
    if (spurningarNumer != spurningar.length) {// Þetta gerist ef spurningarnar eru ekki búnar
        spurningarNumer++;
        setjaUppSpurningu(spurningar[spurningarNumer-1]);
    } else {// Þetta gerist ef spurningaleikurinn er búinn
        clearInterval(skeidklukka);// Þetta stoppar skeiðklukkuna

        let born = Array.from(svaraStadur.children);// Þetta finnur öll svörin og breytir listanum af þeim í Array
        born.forEach(barn => {// Þetta gerist fyrir hvert svar
            // Hérna setti ég bæti vegna þess að mér datt enga enfalda hugmynd í hug til þess að tékka hvort þyrfti eða muna hvort ég ætti að gera og það kemur engin villa frá þessu
            barn.removeEventListener("click",rangtSvar,false);// Þetta eyðir eventListener frá svarmöguleikanum sem er verið að fara í gegnum
            barn.removeEventListener("click",rettSvar,false);// Þetta eyðir eventListener frá svarmöguleikanum sem er verið að fara í gegnum
        });

        spilaAftur.classList.remove("falid");// Þetta lætur spila aftur takkann birtast
    }
}
let rangtSvar = (evt) => {// Þetta er keyrt ef það var ýtt á rangt svar
    rongSvor ++;
    rangraSvaraTexti.textContent = rongSvor;// Textinn uppfærður
    evt.target.style.backgroundColor = "rgb(255,0,0)";// Hérna er bakgrunnslitinum breytt
}

// ----- Sækja JSON skránna -----
fetch(nafnJSON)// Hérna er sótt JSON skránna
    .then(res => res.json())// Hérna er breytt því sem var sótt í Object fyrir JavaScript og það er notað .then til þess að það sé biðið eftir að það sé búið að sækja JSON skránna
    .then(out => {
        // Texta sem breytist aldrei breytt
        fjoldiSpurningaTexti.textContent = out.length;

        out.shuffle();// Þetta ruglar í röð spurninganna

        out.forEach(spurning => {// Þetta keyrir einu sinni fyrir hvern hlut í listanum og bætir hlutnum við arrayin spurningar vegna þess að ef ég gerði spurningar = out þá bjó ég bara til annan private object og gat ekki notað þetta neinstaðar annar staðar
            spurningar.push(spurning);
        });

        setjaUppSpurningu(spurningar[spurningarNumer-1]);
    });

// Gera tagsetningu tilbúna fyrir skeiðklukkuna
let byrjunarDagsetning = new Date().getTime();

// Skeiðklukka sem keyrir 10 sinnum á sekúndu til þess að skeiðklukkan sé allveg rétt
let skeidklukka = setInterval(() => {
    timi = new Date().getTime() - byrjunarDagsetning;// Þetta býr til núverandi tíma og mínusar byrjunartímann frá til þess að fá hversu langt sé síðan leikmaðurinn byrjaði í millisekúndum
    timaTexti.textContent = Math.floor(timi/1000);// Hérna er textinn uppfærður með nýjasta tímanum og ég námunda niður svo að þetta sýni frekar minni tíma heldur en meiri og það þarf að deila með 1000 vegna þess að breytan timi er í millisekúndum
},100);

spilaAfturTakki.addEventListener("click",() => {location.reload();},false);// Þetta endurhleður síðunni þegar notandinn ýtir á þennan eventListener og þá byrjar spurningarleikurinn aftur