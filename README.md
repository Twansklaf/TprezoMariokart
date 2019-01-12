# UE7 - Programmation réseaux

## Architecture

Rapport :

- `report` contient notre rapport.

Serveurs :

- `car.py` contient le code propre à la voiture.
- `remote.py` contient le code propre à la télécommande.
- `centralServer.py` contient le code propre au serveur central.

Helpers :

- `move.py`, `message.py` et `player.py` contiennent du code nécessaire aux trois serveurs.

Paramètres :

- `ip.json` contient les différentes adresses IP à paramétrer.

Librairies externes :

- `xbox.py` contient le code nécessaire à l'utilisation de la manette d'xbox.

## Get started

- Ce code est concu pour être lancé avec python 2.7.x.
- `car.py` s'attend à disposer de la librairie GPIO (et donc à être lancé en root).
- `remote.py` s'attend à être lancé en root pour utiliser la xbox.
