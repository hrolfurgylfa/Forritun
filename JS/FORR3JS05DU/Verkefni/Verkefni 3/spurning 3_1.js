// A
let geimflaug = {
    life: 10,
    speed: 10
}
function GeimflaugaConstructor (nafn) {
    this.nafn = nafn;
}
GeimflaugaConstructor.prototype = geimflaug;

let f1 = new GeimflaugaConstructor("SSE Cydonia");
let f2 = new GeimflaugaConstructor("HMS Deonida");
let f3 = new GeimflaugaConstructor("ISS Covenant");

// B
f1.speed = 4;
f2.speed = 7;
f3.speed = 11;

// C
geimflaug.fly = function() {
    this.speed += 1;
}

// D
f1.setLife = function() {
    this.life += 1;
}