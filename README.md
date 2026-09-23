# C'est quoi Mezzdownloader ? 

Mezzdownloader est un outil dans le terminal qui te permet d'installer des vidéos youtube.

# Comment télécharger Mezzdownloader ?

Pour télécharger le projet afin d'utiliser Mezzdownloader, il vous faudra copier cette commande : 

```bash
winget install --id Git.Git -e --source winget
```

ça installera Git qui vous permettra d'avoir git pour installer le projet, ensuite vous allez faire cette commande : 

```bash
git clone https://github.com/mezzdev/Mezzdownloader
```

Une fois que le projet sera installé, il faudra ouvrir un terminal ( cmd de préférence ) et taper la commande suivante :

```bash
python -m pip install yt-dlp colorama
```

Puis vous allez télécharger le fichier MezzDownloader.py et vous allez dans le terminal ( toujours cmd ) aller dans l'endroit où se trouve le fichier MezzDownloader.py et taper la commande suivante :

```bash
python Mezzdownloader.py
```
