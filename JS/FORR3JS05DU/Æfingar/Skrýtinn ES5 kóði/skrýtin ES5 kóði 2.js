"use strict";
let a = 1;
function b() {
    a = 10;
    return;
function a() {}
}
b();
console.log(a);


//Raðaður rétt
"use strict";
let a = 1;// Breytan a búin til sem 1
b();// Fallið b keyrt
// Farið inn í fall 1
    a = 10;// a breitt í 10 á meðan það er inni í fallinu
    return;// Hérna er farið útúr fallinu svo að fallið a er aldrei búið til og a var aldrei skilað aftur svo að það er enþá 1
console.log(a);// a prentað út og það er enþá 1 hérna