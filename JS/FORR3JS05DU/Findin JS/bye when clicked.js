"use strict";
document.body.addEventListener("click", function(){
    document.write('<h1 style="text-align:center">Bye!</h1>');
    const gamla_document_title = document.title;
    console.log("S: "+gamla_document_title);
    document.title = "Bye!";
    document.body.style.backgroundColor = "blue";
});