import glob
from bs4 import BeautifulSoup
import os

html_dir = "alt" #"path" de fichier 
output_dir = html_dir   

html_files = sorted(glob.glob(os.path.join(html_dir, "*.html"))) # 

for index, html_path in enumerate(html_files, start=1):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser') #Utilisation de "beautifulsoup" 
    alt_texts = [img['alt'] for img in soup.find_all('img') if img.has_attr('alt')]

    out_path = os.path.join(output_dir, f"{index}.txt")
    with open(out_path, 'w', encoding='utf-8') as fo:
        for alt in alt_texts:#
            fo.write(alt + "\n")

    print(f"[{index}] {os.path.basename(html_path)} : {os.path.basename(out_path)}")