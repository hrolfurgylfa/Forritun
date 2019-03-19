"use strict";

// Gera húkka inn í HTML
adal = document.getElementById("adal");

// Föll
let geraItems = (foreldri,...born) => {
    console.log("Foreldri: "+foreldri+"\nBörn: "+born);
}

geraItems(adal,1, 2, 3, 4);