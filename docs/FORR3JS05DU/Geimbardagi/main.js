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
// Stillinga breytur
let staerdSpilaraStilling = 20;
let skotaHradiStilling = 2;
let ovinaSpawnHradiStilling = 500;
let lifStilling = 3;

// Stillinga breytur gerdar
let staerdSpilara = staerdSpilaraStilling;
let skotaHradi = skotaHradiStilling;
let ovinaSpawnHradi = ovinaSpawnHradiStilling;
let lif = lifStilling;

// Auto breytur
let ovinaSpawnTeljari = ovinaSpawnHradi;
let spilaraHitbox = staerdSpilara/1.5;
let ollSkot = [];
let allirOvinir = [];
let buid = false;
let ovinirDrepnir = 0;

//Breytur fyrir setInterval
let adalLoopID;
let ovinirSkjotaID;
let erfidaraID;

// Teljarar
let lifaTexti = document.getElementById("lifaTexti");// Þetta fær elementinn fyrir lífa teljarann svo að það þurfi ekki að gera það oft 
let ovinirDrepnirTexti = document.getElementById("ovinirDrepnirTexti");// Þetta fær elementinn fyrir óvinir drepnir teljarann svo að það þurfi ekki að gera það oft

// Gera takka tilbúinn
let byrjaTakki = document.getElementById("takki");

// Gera canvas tilbúinn
let canvas = document.getElementById("leikur");
let ctx = canvas.getContext('2d');

// ----- Klasar og Objects -----
let Spilari = {
    x: 0,
    y: 0
}
class Skot {
    constructor(x, y, att, litur, origin) {
        this.x = x;
        this.y = y;
        this.att = att;
        this.litur = litur;
        this.originOvinur = origin;
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
    while (ollSkot.length != i) {
        switch (ollSkot[i].att) {
            case "n":
                if (ollSkot[i].y < -35) {// Eyða skoti ef það er farið út af skjánum
                    ollSkot.splice(i, 1);
                    i--;// Þetta er til þess að þegar ég eyði eynum hlut þá fari þetta einn til baka svo að ég hoppi ekki yfir einn hlut í listanum
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
            ollSkot.push(new Skot(ovinur.x, ovinur.y, att, "blue", true));
        }); 
    });
}
let reset = () => {// Þetta fall endurræsir allar nauðsinlegar breytur til þess að það sé hægt að spila aftur
    staerdSpilara = staerdSpilaraStilling;
    skotaHradi = skotaHradiStilling;
    ovinaSpawnHradi = ovinaSpawnHradiStilling;
    lif = lifStilling;
    buid = false;
    ovinirDrepnir = 0;
    allirOvinir = [];
    ollSkot = [];
}

// Collition Detection
let collitionDetection = () => {
    if (ollSkot.length != 0) {
        let i = 0;
        while (ollSkot.length != i) {// Þessi lúppa keyrir þangað til listinn er búinn
            if (ollSkot[i].originOvinur === true) {// Þetta gerist ef skotið sem er verið að fara í gegnum er frá óvini
                if (Spilari.x < ollSkot[i].x + spilaraHitbox && Spilari.x > ollSkot[i].x - spilaraHitbox && Spilari.y < ollSkot[i].y + spilaraHitbox && Spilari.y > ollSkot[i].y - spilaraHitbox) {
                    lif--;
                    ollSkot.splice(i, 1);
                    i--;// Þetta er til þess að þegar ég eyði eynum hlut þá fari þetta einn til baka svo að ég hoppi ekki yfir einn hlut í listanum
                    lifaTexti.textContent = lif;// Þetta lækkar lífa counterinn
                    if (lif === 0) {
                        buid = true;
                    }
                }
            } else if (allirOvinir.length != 0) {// Þetta gerist bara ef það eru skot frá spilaranum á vellinum og það er allavegana einn óvinur á vellinum
                let i2 = 0;// Hérna bý ég til annan teljara til þess að fara í gegnum alla óvinina og sjá hvort að þeir séu búnir að rekast í skot spilarans
                while (allirOvinir.length != i2) {// Þessi lúppa keyrir þangað til listinn er búinn
                    if (allirOvinir[i2].x < ollSkot[i].x + 10 && allirOvinir[i2].x > ollSkot[i].x - 10 && allirOvinir[i2].y < ollSkot[i].y + 10 && allirOvinir[i2].y > ollSkot[i].y - 10) {
                        // Hérna hefur óvinur verið drepinn
                        allirOvinir.splice(i2, 1);
                        i2--;// Þetta er til þess að þegar ég eyði eynum hlut þá fari þetta einn til baka svo að ég hoppi ekki yfir einn hlut í listanum
                        // Hérna bæti ég óvininum við stigin
                        ovinirDrepnir++;
                        ovinirDrepnirTexti.textContent = ovinirDrepnir;
                    }
                    i2++;// Þetta hækkar teljarann um 1 til þess að fara í næsta hlut í listanum
                }
            }
            i++;// Þetta hækkar teljarann um 1 til þess að fara í næsta hlut í listanum
        }
    }
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
    ollSkot.forEach((skot) => {// Þetta gerist fyrir hvert skot
        ctx.strokeStyle = skot.litur;
        ctx.beginPath();
        ctx.moveTo(skot.x, skot.y)
        switch (skot.att) {// Þetta tékkar á áttinni á skotinu og teiknar það í rétta átt
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
    allirOvinir.forEach(ovinur => {// Þetta gerist fyrir hvern óvin
        ctx.beginPath();
        ctx.arc(ovinur.x, ovinur.y, 20, 0, Math.PI*2, false);
        ctx.fill();
        ctx.closePath();
    });
}

// Aðalfall
let adalLoop = () => {// Aðal fallið
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
    collitionDetection();

    //Teikna
    ctx.clearRect(0, 0, canvas.width, canvas.height);// Hreinsa
    teiknaSkot();// Teikna öll skot spilara
    teiknaSpilara(Spilari.x, Spilari.y);// Teikna spilara
    teiknaOvini();// Teikna óvini

    // Tékka hvort að leikurinn sé búinn
    if (buid === true) {
        clearInterval(adalLoopID);// Þetta stoppar setInterval sem kom í byrjun
        clearInterval(ovinirSkjotaID);// Þetta stoppar setInterval sem kom í byrjun
        clearInterval(erfidaraID);// Þetta stoppar setInterval sem kom í byrjun
        ctx.clearRect(0, 0, canvas.width, canvas.height);// Hreinsa
        byrjaTakki.classList.remove("fela");
        byrjaTakki.textContent = "Spila aftur";
        canvas.classList.remove("fela_mus");

        // Skrifa buid texta
        ctx.font = "80px Arial";
        ctx.fillStyle = "red";
        ctx.textAlign = "center";
        ctx.fillText("Þú tapaðir", canvas.width/2, canvas.height/2); 
    }
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
    ollSkot.push(new Skot(Spilari.x, Spilari.y - 15, "n", "red", false));
});

// ----- Byrjun -----
byrjaTakki.addEventListener("click",function() {
    if (canvas.getContext) {
        reset();// Þetta endurræsir allar breytur
        byrjaTakki.classList.add("fela");// Þetta felur spila takkann
        canvas.classList.add("fela_mus");// Þetta felur búsina þegar hún er yfir canvas
        adalLoopID = setInterval(adalLoop,10);
        ovinirSkjotaID = setInterval(ovinirSkjota,1000);
        erfidaraID = setInterval(() => {ovinaSpawnHradi = ovinaSpawnHradi/1.5},2000);// Þetta gerir fleiri óvini yfir tíma
    }
});
