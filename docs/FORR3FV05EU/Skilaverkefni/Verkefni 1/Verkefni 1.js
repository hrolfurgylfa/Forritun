"use strict";

// HTML Krækjur
const svg_image = document.getElementById("emoji_svg");
const emoji = document.getElementById("smily");
const arrow_front = document.getElementById("arrow_front");
const arrow_back = document.getElementById("arrow_back");

// Föll
let enableImageClick = () => {// Þetta fall keyrir eftir ákveðinn tíma og það bætir við onEventListener, þegar hann keyrir spilast animation þar sem fremri patrtur örvarinnar dettur af
    svg_image.addEventListener("click", () => {// Þetta keyrir þegar það er ýtt á myndina og keyrir bara einu sinni
        
        // Hérna reikna ég út hversu langt örin þarf að fara til þess að hverfa niður af skjánum
        let arrow_travel_distance = (window.innerHeight / window.innerWidth) * 200;
        if (arrow_travel_distance < 28) { arrow_travel_distance = 28; }
        
        console.log( "Arrow travel distance: " + arrow_travel_distance ); 
        
        anime({// Þetta er animation þar sem fremri partur örvarinnar dettur af
            targets: [arrow_front],// Þetta er það sem animationin hefur áhrif á
            translateX: [
                { value: "+=150", duration: 1500, delay: 0 },
                { value: "+=0", duration: 1500, delay: 0 }
            ],
            translateY: [
                { value: "-=100", duration: 1500, delay: 0 },
                { value: arrow_travel_distance, duration: 1500, delay: 0 }
            ],
            rotate: [
                { value: "+=60", duration: 1500, delay: 0 }
            ]
        });
    }, { once: true });// Þetta gerir það að verkum að þegar það er búið að keyra þennan event listiner getur hann ekki keyrt aftur
}

// Snúa emoji
anime({
    targets: [emoji],
    rotate: 360,
    duration: 800
});

// Skjóta ör
anime({
    targets: [arrow_front, arrow_back],
    translateX: [-300, 0],
    translateY: [-150, 10],
    rotate: [30, 30],
    duration: 300,
    delay: 1000,
    easing: 'easeInOutQuad'
});

// Passa að það sé ekki látið fremri part örvarinnar detta af of snemma
window.setTimeout(enableImageClick, 1300);
