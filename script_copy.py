# -*- coding:utf8 -*-
# ---------------------------------------------------------------------------
# Name : script_copy.py
# Created on: 2021/03/10
# Author: VIGAN Jéros (Zedauna)
# Usage:
# Description: Copie recursive dossier et fichiers
# ---------------------------------------------------------------------------
#############################
### Package de travail
#############################
import os
import shutil
from datetime import datetime

#############################
### Foncion
#############################
#Copie recursive sous condition booléenne
def copy(filename, source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
        from_path = os.path.join(source, filename)
        to_path = os.path.join(destination, "shape")
    else:
        from_path = os.path.join(source, filename)
        to_path = os.path.join(destination, "shape")

    if os.path.exists(to_path):
        shutil.rmtree(to_path, ignore_errors=True)
        shutil.copytree(from_path, to_path)
        print(' Fin de la copie du dossier ' + filename + ' dans '+to_path)
    else:
        shutil.copytree(from_path, to_path)
        print(' Fin de la copie du dossier ' + filename + ' dans '+to_path)

#Parametre (dossier contenant les fichiers)
source = r"C:\Users\Desktop\from_path"

#############################
### movie
#############################
filename = "movie"
destination = r"C:\Users\Desktop\to_path"

#Debut du programme
debut = datetime.now()

#copy
copy(filename, source, destination)

#fin du programme
fin = datetime.now()

print('la durée totale du traitement  ' + str(fin-debut) + 's')
print('Fin du programme !')