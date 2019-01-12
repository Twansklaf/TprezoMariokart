# UE7 - Programmation réseaux

## Architecture

Servers :

All the code regarding the pi server is inside the final/code_pi_server folder

- `codeserver.py` is the code of the pi server. It allows (when configured correctly) to drive the car with the controller through this server. The pi needs to be an AP.
- `qr.py` runs at the same time than the server and reads info from the pi camera, and writes in billboard.txt when a tag/car is found.
- `display_scores.py` creates a TKinter windows to display the cars arrived by reading billboard.txt.

Car :

All the code regarding the pi server is inside the final/code_pi_voiture folder

- `ex_socket.py` contains all the code that makes the car move
- `switchoffGPIO.py` is run when the car start to prevent the motors from turning indefinitely

Controller :

All the code regarding the pi server is inside the final/code_controller folder

- `controller.py` contains the code specific to the controller. It sends data packets to the server for controlling the car.

External librairies :

- `xbox.py` allows to drive the Xbox Controller
- `Network.py` contains simple functions for packet serialiazation, for sending data structures over a network

## Get started

Run in root.
Run with python 2.7.x