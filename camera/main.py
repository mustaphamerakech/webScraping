import cv2

def convertir_dav_vers_mp4(fichier_dav, fichier_mp4):
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

# Utilisation de la fonction
fichier_dav = "C:/Users/dell/Desktop/dataScienceTp/XVR_ch11_main_20231220162041_20231220170008.dav"
fichier_mp4 = "C:/Users/dell/Desktop/dataScienceTp/video/video7.mp4"
convertir_dav_vers_mp4(fichier_dav, fichier_mp4)
