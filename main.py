import webview
from win10toast import ToastNotifier
import time
import os
import sys
import ctypes
from src.deletecaca import *

toaster = ToastNotifier()
icon_path = os.path.join(os.getcwd(), './img/tgcestmieux.ico')

# Vérifie si le script est exécuté en mode administrateur
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Relance le script en mode administrateur si nécessaire
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()

html_content_pour_sineeep_le_gros = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@lafraude</title>
    <link rel="stylesheet" href="src/public/style.css">
</head>
<body>
    <h1>Bonjour Sineeep le gros</h1>
    <button onclick="deletetzxgrosporcdesineeep()">Clique ici pour delete le cheat</button>
    <p>Choisis le chemin ou se trouve le dossier de cheat, et je m'occupe pour qu'il n'y ait aucune trace</p>
    <img class="gif-container" src="img/CESTPASLAVIEQUEJEVOULAIS.gif" alt="">

    <script>
        function deletetzxgrosporcdesineeep() 
        {
            pywebview.api.delete_tzx_elmorjen();
        }
    </script>
</body>
</html>
"""

html_file_path = "interface.html"

with open(html_file_path, "w") as file:
    file.write(html_content_pour_sineeep_le_gros)

class Api:
    def delete_tzx_elmorjen(self):
        # Demande à l'utilisateur de choisir un dossier via une boîte de dialogue
        folder_path = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG, "Choisissez le dossier à supprimer")
        
        if folder_path:
            folder_path = folder_path[0]  # Récupère le chemin sélectionné
            start(folder_path)  # Appelle la fonction start avec le chemin
            toaster.show_toast("@Lafraude", "Tg sineeep, c'est good normalement wlh", icon_path=icon_path, duration=5)
        else:
            toaster.show_toast("@Lafraude", "Aucun dossier sélectionné, opération annulée.", icon_path=icon_path, duration=5)


def je_run_la_daronne_a_sineeep(): 
    api = Api()
    webview.create_window("@lafraude", html_file_path, js_api=api)
    webview.start()

if __name__ == "__main__":
    je_run_la_daronne_a_sineeep()