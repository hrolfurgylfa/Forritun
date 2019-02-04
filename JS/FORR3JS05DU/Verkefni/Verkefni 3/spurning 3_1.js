let geimflaug = {
    life: 10,
    speed: 10
}
function Geimflaug (nafn) {
    this.nafn = nafn;
    this.__proto__ = geimflaug;
}