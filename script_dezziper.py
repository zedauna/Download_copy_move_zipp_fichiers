# -*- coding:utf8-*-
# ---------------------------------------------------------------------------
# Name : script_dezziper.py
# Created on: 2021/03/08
# Author: VIGAN Jéros (Zedauna)
# Usage:
# Description: Décompression fichiers shapefiles zippés
# ---------------------------------------------------------------------------

#############################
### Package de travail
#############################
import os
from zipfile import ZipFile

#############################
### From et to
#############################
dest_in = r"C:\Users\Desktop\P2"
dest_out = r"C:\Users\Desktop\P2\zip"
os.makedirs(dest_out)

#############################
### movie.zip
#############################
#dossier de depart des fichiers zip
filename = "movie.zip"
path_file_in = os.path.join(dest_in, filename)

#dossier de destination
filename = filename.replace(".zip", "")
path_file_out = os.path.join(dest_out, filename)

#decompression
with ZipFile(path_file_in, 'r') as zip:
  zip.printdir()
  zip.extractall(path_file_out)
  zip.close()

print('Fin de décompression, le dossier ' + filename + ' est prét')

print('Fin du programme !')
