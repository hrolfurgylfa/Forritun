"use strict";

// Þetta gerir mér kleift að fá random hlut úr öllum arreyum
Array.prototype.randomElement = function () {
    return this[Math.floor(Math.random() * this.length)]
}

// Templates
let kort = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
let kubbar_templates = {
    I: [[[0,0,1,0], [0,0,0,0], [0,1,0,0], [0,0,0,0]],
        [[0,0,1,0], [0,0,0,0], [0,1,0,0], [1,1,1,1]],
        [[0,0,1,0], [1,1,1,1], [0,1,0,0], [0,0,0,0]],
        [[0,0,1,0], [0,0,0,0], [0,1,0,0], [0,0,0,0]]],

    J: [[[0,0,1,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
        [[0,0,1,0], [0,1,0,0], [0,1,1,0], [1,1,1,0]],
        [[0,1,1,0], [0,1,1,1], [0,1,0,0], [0,0,1,0]],
        [[0,0,0,0], [0,0,0,0], [0,1,0,0], [0,0,0,0]]],

    L: [[[0,1,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
        [[0,1,0,0], [0,1,1,1], [0,1,1,0], [0,0,1,0]],
        [[0,1,1,0], [0,1,0,0], [0,0,1,0], [1,1,1,0]],
        [[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,0]]],

    O: [[[0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0]],
        [[0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0]],
        [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
        [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]],

    Z: [[[0,1,1,0], [0,0,1,0], [0,1,1,0], [0,0,1,0]],
        [[0,0,1,1], [0,1,1,0], [0,0,1,1], [0,1,1,0]],
        [[0,0,0,0], [0,1,0,0], [0,0,0,0], [0,1,0,0]],
        [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]],

    T: [[[0,0,1,0], [0,0,1,0], [0,1,1,1], [0,0,1,0]],
        [[0,1,1,1], [0,0,1,1], [0,0,1,0], [0,1,1,0]],
        [[0,0,0,0], [0,0,1,0], [0,0,0,0], [0,0,1,0]],
        [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]],

    S: [[[0,0,1,1], [0,1,0,0], [0,0,1,1], [0,1,0,0]],
        [[0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0]],
        [[0,0,0,0], [0,0,1,0], [0,0,0,0], [0,0,1,0]],
        [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]],
}

// Breytur
let tel = 1;
let allirKubbar = ["I","J","L","O","Z","T","S"];
let tetrisKubbur = nyrKubbur(allirKubbar);
let vantarKubb = true;

// Klasar
class Kubbur {
    constructor(id) {
        switch (id) {
            case "I":
                this.bygging = kubbar_templates.I;
                this.litur = "#4ff";
                console.log("I");
                break;
            case "J":
                this.bygging = kubbar_templates.J;
                this.litur = "#f99118";
                console.log("J");
                break;
            case "L":
                this.bygging = kubbar_templates.L;
                this.litur = "#437cfb";
                console.log("L");
                break;
            case "O":
                this.bygging = kubbar_templates.O;
                this.litur = "#f4ff3f";
                console.log("O");
                break;
            case "Z":
                this.bygging = kubbar_templates.Z;
                this.litur = "#15ff44";
                console.log("Z");
                break;
            case "T":
                this.bygging = kubbar_templates.T;
                this.litur = "#ae00f9";
                console.log("T");
                break;
            case "S":
                this.bygging = kubbar_templates.S;
                this.litur = "#f80000";
                console.log("S");
                break;
            
        }
        this.snuningur = 0;
        this.x = 3;
        this.y = 0;
    }
    snua() {
        if (this.snuningur < 3) {
            this.snuningur++;
        } else {
            this.snuningur = 0;
        }
    }
}

// Föll
function adalLoop() {
    console.log(kort);
}

function nyrKubbur() {
    return new Kubbur(allirKubbar.randomElement());
}

setInterval(adalLoop,10);