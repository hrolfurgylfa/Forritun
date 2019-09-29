document.getElementById("secondary").remove();
document.getElementById("comments").remove();

const contents_productive = document.getElementById("primary");
if (contents_productive != null) {
    productive_text_element = document.createElement("h2");
    productive_text = document.createTextNode("Þú ættir að vera að vinna");
    productive_text_element.appendChild(productive_text);
    contents_productive.parentElement.appendChild(productive_text_element);
    contents_productive.remove();
}