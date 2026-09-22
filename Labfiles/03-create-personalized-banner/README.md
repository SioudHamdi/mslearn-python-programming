# Bannière personnalisée

Ce programme demande le nom de l'utilisateur, le transforme en bannière ASCII et affiche un message de bienvenue.

## Dépendance

Le programme utilise le paquet Python `pyfiglet` pour générer la bannière.

Installez-le avec :

```powershell
python -m pip install pyfiglet
```

## Exécution

Depuis ce dossier, lancez :

```powershell
python app.py
```

Le programme demande ensuite :

```text
What is your name?
```

## Fonctionnement

1. `import pyfiglet` charge le paquet de génération de texte ASCII.
2. `input()` demande le nom de l'utilisateur et le stocke dans `name`.
3. `pyfiglet.figlet_format(name)` transforme le nom en bannière.
4. `print(banner)` affiche la bannière.
5. `name.upper()` convertit le nom en majuscules dans le message de bienvenue.

## Personnaliser la police

Pour utiliser une autre police, transmettez son nom avec l'argument `font` :

```python
banner = pyfiglet.figlet_format(name, font="slant")
```

Pour afficher les polices disponibles :

```python
from pyfiglet import FigletFont

print(FigletFont.getFonts())
```
