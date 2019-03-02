"use strict";

// Þetta gerir mér kleift að fá random hlut úr öllum arreyum
Array.prototype.randomElement = function() {
    return this[Math.floor(Math.random() * this.length)]
}
// Þetta skilar random tölu á milli talnana sem fara inn
let FaRandomTolu = (min, max) => {
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
    constructor(x, y, att, litur) {
        this.x = x;
        this.y = y;
        this.att = att;
        this.litur = litur
    }
}
class Ovinir {
    constructor() {
        this.x = FaRandomTolu(15,575);
        this.y = FaRandomTolu(15,200);
    }
}

// ----- Föll -----
// Physics föll
let faeraSkot = () => {
    let i = 0;
    while (true) {
        switch (ollSkot[i].att) {
            case "n":
                if (ollSkot[i].y < -35) {// Eyða skoti ef það er farið út af skjánum
                    ollSkot.splice(i, 1);
                    i--;
                } else {
                    ollSkot[i].y -= skotaHradi;// Færa skotið
                }
                break;
            case "s":
                if (ollSkot[i].y > 635) {// Eyða skoti ef það er farið út af skjánum
                    ollSkot.splice(i, 1);
                    i--;
                } else {
                    ollSkot[i].y += skotaHradi;// Færa skotið
                }
                break;
            case "v":
                if (ollSkot[i].x < -35) {// Eyða skoti ef það er farið út af skjánum
                    ollSkot.splice(i, 1);
                    i--;
                } else {
                    ollSkot[i].x -= skotaHradi;// Færa skotið
                }
                break;
            case "a":
                if (ollSkot[i].x > 635) {// Eyða skoti ef það er farið út af skjánum
                    ollSkot.splice(i, 1);
                    i--;
                } else {
                    ollSkot[i].x += skotaHradi;// Færa skotið
                }
                break;
        }
        if (ollSkot.length - 1 === i) {// Þetta lokar lúpunni ef listinn er búinn
            break;
        }
        i++;
    }
}
let ovinaStjorn = () => {
    allirOvinir.forEach(ovinur => {
        let leyfdarHreyfingarOvina = [];
        if (ovinur.x > 20) {leyfdarHreyfingarOvina.push("v");}
        if (ovinur.x < 580) {leyfdarHreyfingarOvina.push("a");}
        if (ovinur.y > 20) {leyfdarHreyfingarOvina.push("n");}
        if (ovinur.y < 180) {leyfdarHreyfingarOvina.push("s");}
        let hreyfing = leyfdarHreyfingarOvina.randomElement();
        if (hreyfing === "n") {ovinur.y -= 10;}
        else if (hreyfing === "s") {ovinur.y += 10;}
        else if (hreyfing === "v") {ovinur.x -= 10;}
        else if (hreyfing === "a") {ovinur.x += 10;}  
    });
}
let buaTilOvin = () => {
    allirOvinir.push(new Ovinir());
}
let ovinirSkjota = () => {
    allirOvinir.forEach(ovinur => {
        ["n","s","a","v"].forEach(att => {
            ollSkot.push(new Skot(ovinur.x, ovinur.y, att, "blue"));
        }); 
    });
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
    ollSkot.forEach((skot) => {
        ctx.strokeStyle = skot.litur;
        ctx.beginPath();
        ctx.moveTo(skot.x, skot.y)
        switch (skot.att) {
            case "n":
                ctx.lineTo(skot.x, skot.y + 30);
                break;
            case "s":
                ctx.lineTo(skot.x, skot.y - 30);
                break;
            case "v":
                ctx.lineTo(skot.x + 30, skot.y);
                break;
            case "a":
                ctx.lineTo(skot.x - 30, skot.y);
                break;
        }
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
    // Hreyfingar
    if (ollSkot.length > 0) {faeraSkot();}// Færa öll skot spilara ef það eru eitthver skot á skjánum
    if (ovinaSpawnHradi <= ovinaSpawnTeljari) {
        buaTilOvin();
        ovinaSpawnTeljari = 0;
    } else {
        ovinaSpawnTeljari++;
    }
    if (allirOvinir.length > 0) {ovinaStjorn();}// Færa alla óvini ef það eru eitthverjir óvinir á skjánum

    // Collition detection

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
    ollSkot.push(new Skot(Spilari.x, Spilari.y - 15, "n", "red"));
});

// ----- Byrjun -----
//byrjaTakki.addEventListener("click",function() {
    if (canvas.getContext) {
        setInterval(adalLoop,10);
        setInterval(ovinirSkjota,1000);
    }
//});
