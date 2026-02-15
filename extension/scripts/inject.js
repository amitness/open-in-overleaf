'use strict';

var BACKEND_URL = 'https://amitness-open-in-overleaf.hf.space'

function getZipURL() {
    return "https://www.overleaf.com/docs?snip_uri=" + BACKEND_URL + "/fetch_tar?arxiv_url=" + encodeURIComponent(document.location.href);
}


function addOverleafButton() {
    var otherFormats = document.getElementsByClassName("abs-button download-pdf")[0];
    var ul = otherFormats.parentElement.parentElement;
    
    // Add link
    var li = document.createElement("li");
    var a = document.createElement('a');
    var linkText = document.createTextNode("Open in Overleaf");
    a.appendChild(linkText);
    a.href = getZipURL();
    li.appendChild(a);
    ul.appendChild(li);
}



addOverleafButton()
