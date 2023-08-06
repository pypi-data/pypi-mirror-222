# MotiPy

Un package Python qui génére des messages de motivation

## Installation

Installez le package à l'aide de `pip` :

```bash
pip install motipy
```

## Utilisation
Importez le package dans votre script Python et appelez la fonction moty() pour obtenir des informations intéressantes :

```bash
import motipy
from motipy.motipy import moty

# Créez le générateur de messages de motivation
motivation = moty()

# Obtenez les messages de motivation à l'aide de la fonction next()
message1 = next(motivation)
print(message1)

message2 = next(motivation)
print(message2)

message3 = next(motivation)
print(message3)
```
Chaque appel à next(motivation_generator) renverra le message de motivation suivant dans la liste mélangée. Vous pouvez ainsi obtenir autant de messages de motivation que vous le souhaitez en utilisant next() à chaque nouvel appel.

## Exigences
- Python3
- <br clear="both">

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="100" alt="python logo"  />
</div>