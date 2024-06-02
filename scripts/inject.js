'use strict';

var BACKEND_URL = 'https://amitness-open-in-overleaf.hf.space'

function convertToZip() {
    // Blur the page to show that conversion is in progress
    var overleafTextElement = document.getElementById("overleaf-text");
    var arxivHeader = document.getElementById("header");
    overleafTextElement.textContent = "Converting...";
    document.body.style.filter = 'blur(2px)';
    arxivHeader.style.background = "#4f9c45";

    // Perform an API call to convert the .tar.gz file to a zip file
    fetch(BACKEND_URL + "/run/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            data: [
                document.location.href
            ]
        })
    })
        .then(r => {
            if (!r.ok) {
                throw new Error('Network response was not ok');
            }
            return r.json();
        })
        .then(
            r => {
                var zip_name = r.data[0]['zip_url'];
                var latex_zip_url = BACKEND_URL + "/file=" + zip_name;

                // Redirect to overleaf pointing to the zip file
                window.location = "https://www.overleaf.com/docs?snip_uri=" + latex_zip_url;
            }
    )
        .catch(error => {
            setTimeout(() => {
                overleafTextElement.textContent = "Open in Overleaf";
            }, 3000);
            overleafTextElement.textContent = "Failed. Please try again in few minutes...";
            document.body.style.filter = 'none';
            arxivHeader.style.background = "#b31b1b";
        });
}


function addOverleafButton() {
    var otherFormats = document.getElementsByClassName("abs-button download-pdf")[0];
    var ul = otherFormats.parentElement.parentElement;
    
    // Create a clickable link
    var li = document.createElement("li");
    var a = document.createElement('a');
    var linkText = document.createTextNode("Open in Overleaf");
    a.appendChild(linkText);
    a.href = "#";
    a.setAttribute("id", "overleaf-text");

    li.appendChild(a);
    li.addEventListener("click", convertToZip);
    ul.appendChild(li);
}



addOverleafButton()
