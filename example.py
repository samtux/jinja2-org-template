#!/usr/bin/env python3
# Author: Samuel Mesa <samuelmesa etal linuxmail.org>
# Date: April 18, 2022

import jinja2
from emacs import EmacsBatch
import matplotlib.pyplot as plt
import numpy as np

templateLoader = jinja2.FileSystemLoader(searchpath='./')
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = 'example.j2'
ORG_FILE = 'example.org'
IMG_FILE = 'bar.png'
template = templateEnv.get_template(TEMPLATE_FILE)
TITLE = "The best operating system"
ITEMS = [
    {'software': 'Office', 'windows': 'Office Windows', 'linux': 'LibreOffice'},
    {'software': 'IDE', 'windows': 'Visual Studio Code', 'linux': 'Doom Emacs'},
    {'software': 'Drive', 'windows': 'Onedrive', 'linux': 'Nextcloud'}
]

x = np.array(['Linux', 'Windows', 'Other'])
y = np.array([90, 8, 2])
plt.bar(x, y)
plt.suptitle(TITLE)
plt.xlabel("OS")
plt.ylabel("Best")
plt.savefig(IMG_FILE)
plt.close()

outputText = template.render(title=TITLE, items=ITEMS, img=IMG_FILE)

with open(ORG_FILE, 'w') as filename:
    filename.write(outputText)

emacs = EmacsBatch()
emacs.run([ORG_FILE, "-f",  "org-latex-export-to-pdf"])
