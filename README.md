<img src="./images/icon.png" align="right" width="75" height="75">

# open-in-overleaf [![Chrome Web Store](https://img.shields.io/chrome-web-store/users/oikhlgfcmfbbdjbeeaplalpfdgijbdji?label=users)](https://chromewebstore.google.com/detail/open-in-overleaf/oikhlgfcmfbbdjbeeaplalpfdgijbdji?pli=1) [![](https://img.shields.io/chrome-web-store/rating/oikhlgfcmfbbdjbeeaplalpfdgijbdji.svg)](https://chromewebstore.google.com/detail/open-in-overleaf/oikhlgfcmfbbdjbeeaplalpfdgijbdji?pli=1)

A browser extension to open and edit any arxiv.org paper directly on overleaf.

https://github.com/amitness/open-in-overleaf/assets/8587189/faaf9ce9-3ab1-410b-af26-dd17afc32211



This is useful to examine how some feature or typesetting effect in a paper was implemented in LaTex. It's also useful to copy equations, citations and tables from the paper for derivative work or presentations.

## Install
- [Chrome Web Store](https://chrome.google.com/webstore/detail/open-in-overleaf/oikhlgfcmfbbdjbeeaplalpfdgijbdji)

## Usage
On the arxiv page, click `Open in Overleaf` link on the sidebar and the latex source code will open up in overleaf. The `Open in Overleaf` link is not shown for papers where the authors haven't uploaded the latex source.

<img width="255" alt="image" src="https://user-images.githubusercontent.com/8587189/233186434-8ff96d82-713d-4dc2-8202-c9026c765e71.png">

## How it works
1. Arxiv provides a latex source for each paper in a `.tar.gz` format
2. Overleaf provides an [API endpoint](https://www.overleaf.com/devs) to open a latex project with a direct link to a zip file
3. Our extension converts the `.tar.gz` file from arxiv to a zip file using a backend service hosted on huggingface spaces [here](https://huggingface.co/spaces/amitness/open-in-overleaf)
4. We then redirect the user to the overleaf page with that url
