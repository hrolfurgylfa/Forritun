"use strict";

/*
Hvernig þetta virkar hjá mér

Þegar notandinn smellir á nav barinn þá er einn eventListiner að bíða og svo tek ég .textContent-ið
úr því og nota það sem ID til þess að finna svo hvaða myndir eiga að birtast.
*/

// Föll
let buaTilMynd = (URL, Utskyringar_texti, ...Flokkar) => {// Þetta fall er til þess að gera það einfaldara fyrir mig að harðkóða myndirnar
    let mynd = {// Hérna er búið til object sem ég bæti svo við í allar myndir arrayinn
        URL: URL,
        Utskyringar_texti: Utskyringar_texti,
        Flokkar: Flokkar
    };
    allarMyndir.push(mynd);// Hérna ýti ég objectinum sem ég bjó til í arrayinn fyrir allar myndirnar
}

let skiptaUmBladsidu = (evt) => {// Þetta fall keyrir í hvert skipti sem notandinn ýtir á nav barinn, tékkar hvað var ýtt á og keyrir svo kóða til þess að sýna réttar myndir
    if (evt.target === nav) {return;}// Þetta fer til baka ef það var ýtt framhjá tökkunum

    // Hérna er ég viss um að notandinn ýtti á eitthvern af tökkunum

    while (true) {// Þetta eyðir öllum börnum mynda_container til þess að gera tilbúið fyrir nýjar myndir
        if (mynda_container.firstChild) {
            mynda_container.firstChild.remove();
        } else {// Þetta sér um að ef öll börnin eru farin þá hætti lúppan
            break;
        }
    }

    let valinDeild = evt.target.textContent;// Hérna geymi ég nafnið á flokknum sem var ýtt á til þess að sýna myndir úr rétta flokknum

    if (valinDeild === "Sýna allt") {// Þetta keyrir ef það var ýtt á allar myndir
        allarMyndir.forEach(mynd => {// Þetta keyrir einu sinni fyrir hverja mynd og keyrir fallið sinaMynd með myndina
            sinaMynd(mynd);
        });
    } else {// Þetta keyrir ef það var ýtt á eitthvað annað en sýna allt og þá þarf að vera tékkað á hverju einustu mynd hvort að hún eigi að vera sýnd
        allarMyndir.forEach(mynd => {
            if (mynd.Flokkar.indexOf(valinDeild) >= 0) {// Þetta tékkar hvort að eitthvað ákveðið sé í array
                sinaMynd(mynd);
            }
        });
    }
}

let sinaMynd = (mynd) => {// Þetta fall bætir mynd við mynda containerinn
    let ny_mynd = new Image(200,200);// Þetta býr til nýja mynd með x: 200 og y: 200
    ny_mynd.src = mynd.URL;// Þetta bætir linkinum fyrir myndina á html elementin
    ny_mynd.alt = mynd.Utskyringar_texti;// Þetta bætir alt textanum fyrir myndina á html elementin

    mynda_container.appendChild(ny_mynd);// Þetta bætir myndinni við sem barni af mynda containerinum
}

// Breytur
let allarMyndir = [];// Hérna bý ég til lista fyrir allar myndirnar

// Búa til myndir
buaTilMynd("Myndir/m1.jpg", "Kanína", "Animators", "Illustrators");
buaTilMynd("Myndir/m2.jpg", "Sjór", "Photographers", "Filmmakers");
buaTilMynd("Myndir/m3.jpg", "Hreindýr", "Photographers", "Filmmakers");
buaTilMynd("Myndir/m4.jpg", "New York götu kort", "Designers");
buaTilMynd("Myndir/m5.jpg", "Trompet spilari", "Photographers", "Filmmakers");
buaTilMynd("Myndir/m6.jpg", "Typographic Study", "Designers", "Illustrators");
buaTilMynd("Myndir/m7.jpg", "Reiðhjól í Japan", "Photographers");
buaTilMynd("Myndir/m8.jpg", "Aqua vörumerki", "Designers");
buaTilMynd("Myndir/m9.jpg", "Draugur", "Animators", "Illustrators");

// Sækja króka úr HTML
const nav = document.getElementById("nav");
const mynda_container = document.getElementById("mynda_container");

// Hérna bæti ég við eventListener til þess að býða eftir að notandinn ýti á nav barinn
nav.addEventListener("click", skiptaUmBladsidu, false);