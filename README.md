🎵 Music Pipeline

Un mini-projet Python permettant de créer des pipelines de traitement audio simples. Ce script utilise pydub pour la manipulation audio et PyYAML pour définir les étapes de traitement dans un fichier de configuration.

🚀 Fonctionnalités

    Chargement de fichiers : Importe des fichiers .wav en tant que pistes audio.

    Traitement modulaire : Applique une série d'effets audio de manière séquentielle.

    Exportation : Exporte les pistes audio résultantes dans le format souhaité.

    Configuration facile : Les pipelines sont définis dans un fichier orchestration.yml facile à lire.

Effets disponibles

    effet_echo : Ajoute un écho simple à la piste.

    effet_inverser : Inverse la piste audio (lecture à l'envers).

    effet_combiner : Superpose (combine) toutes les pistes en une seule.

📦 Prérequis

Avant de commencer, assurez-vous d'avoir Python 3 installé sur votre système.

Ce projet nécessite également FFmpeg, car pydub l'utilise en arrière-plan pour la manipulation audio.

Installation de FFmpeg :

    Sur Linux (Debian/Ubuntu) :
    Bash

sudo apt update
sudo apt install ffmpeg

Sur macOS (avec Homebrew) :
Bash

    brew install ffmpeg

    Sur Windows : Téléchargez les binaires sur le site officiel de FFmpeg et ajoutez-les à votre PATH système.

🛠️ Installation

    Clonez ce dépôt :
    Bash

git clone https://github.com/smuller59/Music_pipeline.git
cd Music_pipeline

Installez les dépendances Python requises :
Bash

pip install -r requirements.txt

(Note : Si vous n'avez pas de requirements.txt, créez-en un ou installez les paquets manuellement)
Bash

    pip install pydub pyyaml

⚙️ Utilisation

Le projet est piloté par le fichier orchestration.yml. C'est là que vous définissez les étapes de votre traitement audio.

1. Préparez vos fichiers audio

Placez les fichiers .wav que vous souhaitez traiter dans le dossier du projet (ou spécifiez leur chemin complet dans le YAML).

2. Configurez orchestration.yml

Ouvrez le fichier orchestration.yml et définissez vos pipelines. Un pipeline est une liste d'étapes.

Structure des étapes :

    load : (Liste de chemins) Charge les fichiers audio initiaux.

    step : (String) Le nom de la fonction d'effet à appliquer (doit être dans le REGISTRY).

    params : (Dictionnaire) Les paramètres optionnels à passer à la fonction d'effet (ex: delai: 1000).

    export : (Liste de chemins) Exporte les pistes audio résultantes vers les fichiers spécifiés.

Exemple de orchestration.yml :
YAML

pipeline_principal:
  - load:
      - "audio/guitare.wav"
      - "audio/batterie.wav"
  - step: "effet_combiner"
  - step: "effet_echo"
    params:
      delai: 250
  - export:
      - "sortie/mix_final_echo.mp3"

pipeline_inverser:
  - load:
      - "audio/voix.wav"
  - step: "effet_inverser"
  - export:
      - "sortie/voix_inversee.wav"

3. Exécutez le pipeline

Lancez le script principal depuis votre terminal :
Bash

python pipeline.py

Le script lira le fichier orchestration.yml, exécutera tous les pipelines définis et créera les fichiers de sortie dans les dossiers spécifiés.