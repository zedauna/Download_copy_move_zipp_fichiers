# -*- coding:utf8 -*-
# ---------------------------------------------------------------------------
# Name : script_telechargement.py
# Created on: 2021/03/08
# Author: VIGAN Jéros (Zedauna)
# Usage:
# Description: Connexion , téléchargement des fichiers shapefiles
# ---------------------------------------------------------------------------
#############################
### Package de travail
#############################
import os
from ftplib import FTP
from datetime import datetime

#############################
### Déclaration des variables
#############################
#Parametres du FTP (à remplir!)
host = "geo-ftp.ongr.fr"
adresseftp = "geo-ftp.ongr.fr"
port_ftp = 8083
user = input('veuillez entrer votre nom d\'utilisateur:')
password = input('veuillez entrer votre mot de passe :')

#Dossier de reception commun aux telechargement
dest_dir = r"C:\Users\Desktop\P2\download"

#############################
### Fonctions
#############################
#connexion
def ftp_connect(adresseftp, user, password, port_ftp):
  ftp = FTP()
  ftp.connect(adresseftp, port_ftp)
  ftp.login(user, password)
  return ftp

#fermeture
def ftp_fermer(ftp):
  try:
    ftp.quit()
  except:
    ftp.close()

#Debut du programme
debut = datetime.now()

#################################
### movie.zip
#################################
#ouverture de la session
ftp = ftp_connect(adresseftp, user, password, port_ftp)
start = datetime.now()

#Positionner dans le repertoire des fichiers sur le serveur
repref = "ftp/commun/endo/geodata/shape"

##Position et liste des fichiers
ftp.cwd(repref)
ftpDir = ftp.pwd()
ftp.dir()

## fichiers à télécharger et dossier de reception
filename = "movie"
path_file_out = os.path.join(dest_dir, filename)

#Téléchargement
handle = open(path_file_out, 'wb')
print("Downloading...: %s" % filename)
ftp.retrbinary('RETR %s' % filename, handle.write)
print("Téléchargement de %s terminé" % filename)

#fermeture de la session
ftp_fermer(ftp)
end = datetime.now()
diff = end - start
print('la durée de téléchargement est ' + str(diff.seconds) + 's')

#fin du programme
fin = datetime.now()

print('la durée totale du traitement est  ' + str(fin-debut) + 's')
print("Fin du programme !")