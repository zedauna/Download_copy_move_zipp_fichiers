# -*- coding:uft8 -*-
# ---------------------------------------------------------------------------
# Name : script_dezziper2.7.py
# Created on: 2021/03/08
# Author: VIGAN Jéros (Zedauna)
# Usage:
# Description: Décompression fichiers shapefiles zippés
# ---------------------------------------------------------------------------

#############################
### Package de travail
#############################
import os
import zipfile

#############################
### From et to
#############################

dest_in = r"C:\Users\Desktop\P2"
dest_out = r"C:\Users\Desktop\P2\zip4"
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
zipfile.ZipFile(path_file_in).extractall(path_file_out)
print('Fin de décompression, le dossier ' + filename + ' est prét')

print('Fin du programme !')
