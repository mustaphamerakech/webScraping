import cv2
import os

def convertir_dav_vers_mp4(fichiers_dav, dossier_sortie):
    for fichier_dav in fichiers_dav:
        # Construire le chemin du fichier de sortie MP4
        nom_fichier = os.path.splitext(os.path.basename(fichier_dav))[0]
        fichier_mp4 = os.path.join(dossier_sortie, f"{nom_fichier}.mp4")

        # Ouvrir le fichier vidéo DAV
        video_dav = cv2.VideoCapture(fichier_dav)

        # Récupérer les propriétés vidéo
        largeur = int(video_dav.get(3))
        hauteur = int(video_dav.get(4))
        fps = video_dav.get(5)

        # Définir le codec et créer un objet VideoWriter
        codec = cv2.VideoWriter_fourcc(*'mp4v')  # Vous pouvez essayer aussi 'mp4v', 'XVID', ou 'MJPG'
        video_mp4 = cv2.VideoWriter(fichier_mp4, codec, fps, (largeur, hauteur))

        # Lire chaque frame et l'écrire dans le fichier MP4
        while True:
            ret, frame = video_dav.read()
            if not ret:
                break
            video_mp4.write(frame)

        # Libérer les ressources
        video_dav.release()
        video_mp4.release()

        print(f"Conversion terminée. Fichier MP4 sauvegardé sous {fichier_mp4}")

# Utilisation de la fonction avec plusieurs fichiers DAV
dossier_entree = "C:/Users/dell/Desktop/dataScienceTp/last"
dossier_sortie = "C:/Users/dell/Desktop/dataScienceTp/video1/"
extensions_dav = [".dav"]

# Récupérer tous les fichiers DAV dans le dossier d'entrée
fichiers_dav = [fichier for fichier in os.listdir(dossier_entree) if os.path.splitext(fichier)[1].lower() in extensions_dav]

# Convertir tous les fichiers DAV
convertir_dav_vers_mp4([os.path.join(dossier_entree, fichier) for fichier in fichiers_dav], dossier_sortie)
