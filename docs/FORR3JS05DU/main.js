"use strict";

let canvas = document.getElementById('leikur');

if (canvas.getContext) {
    let ctx = canvas.getContext('2d');

    //Kassi 1
    ctx.fillStyle = 'rgb(200, 0, 0)';
    ctx.fillRect(100, 100, 50, 50);

    // //Kassi 2
    // ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
    // ctx.fillRect(125, 125, 50, 50);

    //Margir kassar
    let liturRaudur = true;
    let liturGraenn = false;
    let liturBlar = false;
    for (let x = 25; x += 25; x > 480 ) {
        if (liturRaudur === true) {
            ctx.fillStyle = 'rgba(200, 0, 0, 0.5)';
            liturRaudur = false;
            liturGraenn = true;
        } else if (liturGraenn === true) {
            ctx.fillStyle = 'rgba(0, 200, 0, 0.5)';
            liturGraenn = false;
            liturBlar = true;
        } else if (liturBlar === true) {
            ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
            liturBlar = false;
            liturRaudur = true;
        }
        ctx.fillRect(x, x, 50, 50);
    }
}