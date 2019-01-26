"use strict";

let manneskja = {
    nafn: "Jón Jónsson",
    kennitala: 2505004790,
    heimilisfang: " 1",
    heimasími: 5550357,
    farsími: 7385023
};

for (let eiginleiki in manneskja) {
    console.log(eiginleiki + ": " + manneskja[eiginleiki])
}

let manneskja2 = {
    nafn: "Jón Jónsson",
    aldur: 18,// Það var enginn aldur í lið 1 svo að ég bætti honum bara við hérna svo að ég gæti kallað í hann
    kennitala: 2505004790,
    heimilisfang: " 1",
    heimasími: 5550357,
    farsími: 7385023,
    nafnOgAldur : function() {
        console.log(this.nafn+",");
        console.log(this.aldur);
        return;
    }
};

manneskja2.nafnOgAldur()