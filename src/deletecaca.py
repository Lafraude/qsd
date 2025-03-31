import os
import shutil
import ctypes
from win10toast import ToastNotifier

toaster = ToastNotifier()
icon_path = os.path.join(os.getcwd(), './img/tgcestmieux.ico')


def clear_windows_cache(folder_path):
    try:
        temp_dir = os.getenv('TEMP')
        if temp_dir and os.path.exists(temp_dir):
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    if folder_path in file_path:
                        os.remove(file_path)
        print("Cache Windows nettoyé.")
    except Exception as e:
        print(f"Erreur lors du nettoyage du cache Windows : {e}")
        toaster.show_toast("@Lafraude", "Erreur lors du nettoyage du cache Windows", icon_path=icon_path, duration=5)

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path, ignore_errors=True)
        print(f"Dossier supprimé : {folder_path}")
        
        clear_windows_cache(folder_path)
    except Exception as e:
        print(f"Erreur lors de la suppression du dossier : {e}")

def main(folder_path):
    if folder_path and os.path.exists(folder_path):
        delete_folder(folder_path)
    else:
        print("Chemin invalide ou aucun dossier trouvé.")
        toaster.show_toast("@Lafraude", "Chemin invalide ou aucun dossier trouvé.", icon_path=icon_path, duration=5)

def start(folder_path):
    if ctypes.windll.shell32.IsUserAnAdmin():
        if folder_path and os.path.exists(folder_path):
            main(folder_path)
        else:
            print("Chemin invalide ou aucun dossier trouvé.")
            toaster.show_toast("@Lafraude", "Chemin invalide ou aucun dossier trouvé.", icon_path=icon_path, duration=5)
    else:
        print("Veuillez exécuter ce script en tant qu'administrateur.")
        toaster.show_toast("@Lafraude", "Veuillez exécuter ce script en tant qu'administrateur.", icon_path=icon_path, duration=5)
