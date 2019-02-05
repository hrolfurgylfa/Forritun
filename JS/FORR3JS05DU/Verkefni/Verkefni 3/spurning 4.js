// A
class Geimflaug {
    constructor(nafn) {
        this.nafn = nafn;
        this.speed = 10;
        this.life = 10;
    }
    // C
    fly() { this.speed += 1; }
}

let f1 = new Geimflaug("SSE Cydonia");
let f2 = new Geimflaug("HMS Deonida");
let f3 = new Geimflaug("ISS Covenant");

// B
f1.speed = 4;
f2.speed = 7;
f3.speed = 11;

// D
f1.setLife = () => this.life += 1;

