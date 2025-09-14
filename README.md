# projet classifer html et image (Stagiaire de CERES)

L'object du projet:
L'object de ce projet est l'création d'un pipeline par Mots clés d'image sur Google. Il s`agit d'extraire et de classifier le contenu html ainsi que les images associées aux mot de clés, afin de détecter des cas potentiels de désinformation visuelle en line avec article.pdf.

Projet 1 extrait html et image:'code projet1 stage.ipynb'

1. utilisation google API sur python : https://serpapi.com

2. Avoir les resultats sur python et stoker dans le fichier

3. Extrait la balise image

4. Utilisation panoptic. : https://github.com/CERES-Sorbonne/Panoptic

code projet1_2.py

ce code pour extrait des balises "alt"

1. utilisation de beautifulsoup.

2. stocker la balise de chaque html

Le projet suivant.

Pour extraire le code HTML incluant l’image principale, j’utiliserai TinEye.

https://tineye.com
https://ehne.fr/fr

------------------------------English----------------------------------

Project objective:
The objective of this project is to create a pipeline for retrieving images on Google using keywords. It consists in extracting and classifying the HTML content as well as the images associated with these keywords, in order to detect potential cases of visual disinformation, in connection with article.pdf.

Project 1 – HTML & Image Extraction

Notebook: code_projet1_stage.ipynb

Use Google Search API in Python via SerpApi: https://serpapi.com
1. Fetch the results in Python

2. Store them in a file.

3. Extract the img tags

4. Identify the main image with panoptic


Project 1.2 – Alt‑Text Extraction Script: code_projet1_2.py

1. Parse HTML with BeautifulSoup

2. Collect every alt attribute

3. Store each HTML tag’s alt text for later use.

Next Steps

To extract the HTML snippet containing the principal image, I’ll leverage TinEye.

임정민

프로젝트 HTML 과 이미지 추출  beautifulsoup, os, google api 검색엔진 틴아이, sorbonne CERS panoptic 사용

