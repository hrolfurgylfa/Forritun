"use strict";

// Þetta gerir mér kleift að fá random hlut úr öllum arreyum
Array.prototype.randomElement = () => {
    return this[Math.floor(Math.random() * this.length)]
}
// Þetta skilar random tölu á milli talnana sem fara inn
let getRandomInt = (min, max) => {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

// ----- Breytur -----
let staerdSpilara = 20;
let ollSkot = [];
let allirOvinir = [];
let ollOvinaSkot = [];
let skotaHradi = 2;
let ovinaSpawnHradi = 1000;
let ovinaSpawnTeljari = 1000;

// Gera takka tilbúinn
let byrjaTakki = document.getElementById("takki");

// Gera canvas tilbúinn
let canvas = document.getElementById("leikur");
let ctx = canvas.getContext('2d');

// ----- Klasar -----
class Spilari {
    constructor() {
        this.x = 0;
        this.y = 0;
    }
}
class Skot {
    constructor() {
        this.x = Spilari.x;
        this.y = Spilari.y - 15;
    }
}
class Ovinir {
    constructor() {
        this.x = 0;
        this.y = 0;
    }
}

// ----- Föll -----
// Physics föll
let faeraSkot = () => {
    let i = 0;
    while (true) {
        if (ollSkot[i].y < -35) {// Eyða skoti ef það er farið út af skjánum
            ollSkot.splice(i, 1);
            i--;
        } else {
            ollSkot[i].y -= skotaHradi;// Færa skotið
        }
        if (ollSkot.length - 1 === i) {// Þetta lokar lúpunni ef listinn er búinn
            break;
        }
        i++;
    }
}
let ovinaStjorn = () => {
    
}
let buaTilOvin = () => {
    allirOvinir.push(new Ovinir());
    console.log("ovinur");
}

// Teikni föll
let teiknaSpilara = (x, y) => {
    ctx.fillStyle = "black";
    ctx.beginPath();
    ctx.moveTo(x, y - staerdSpilara);
    ctx.lineTo(x + staerdSpilara, y + staerdSpilara);
    ctx.lineTo(x - staerdSpilara, y + staerdSpilara);
    ctx.fill();
}
let teiknaSkot = () => {
    ctx.lineWidth = 10;
    ctx.strokeStyle = "#FF0000";
    ollSkot.forEach((skot) => {
        ctx.beginPath();
        ctx.moveTo(skot.x, skot.y)
        ctx.lineTo(skot.x, skot.y + 30);
        ctx.stroke();
    });
}
let teiknaOvini = () => {
    ctx.fillStyle = "green";
    allirOvinir.forEach(ovinur => {
        ctx.beginPath();
        ctx.arc(ovinur.x, ovinur.y, 20, 0, Math.PI*2, false);
        ctx.fill();
        ctx.closePath();
    });
}

// Aðalfall
let adalLoop = () => {
    // Physics
    if (ollSkot.length > 0) {faeraSkot();}// Færa öll skot spilara ef það eru eitthver skot á skjánum
    if (ovinaSpawnHradi <= ovinaSpawnTeljari) {
        buaTilOvin();
        ovinaSpawnTeljari = 0;
    } else {
        ovinaSpawnTeljari++;
    }

    //Teikna
    ctx.clearRect(0, 0, canvas.width, canvas.height);// Hreinsa
    teiknaSkot();// Teikna öll skot spilara
    teiknaSpilara(Spilari.x, Spilari.y);// Teikna spilara
    teiknaOvini();
}

// ----- Uppákomu hlustarar -----
// Uppfæra músastaðsetninguna
canvas.addEventListener("mousemove", (evt) => {
    let rect = canvas.getBoundingClientRect();
    Spilari.x = evt.clientX - rect.left;
    Spilari.y = evt.clientY - rect.top;
});
// Búa til skot þegar spilarinn ýtir á músina
canvas.addEventListener("click", () => {
    ollSkot.push(new Skot());
    // console.log(ollSkot);
});

// ----- Byrjun -----
//byrjaTakki.addEventListener("click",function() {
    if (canvas.getContext) {
        setInterval(adalLoop,10);
    }
//});
