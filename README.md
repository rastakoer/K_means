La segmentation d'image est le processus de partitionnement d'une image en plusieurs régions différentes. L'objectif est de changer la représentation de l'image en une image plus simple et plus significative.

C'est une étape importante dans le traitement d'image, car les images du monde réel ne contiennent pas toujours un seul objet que nous voulons classer. Par exemple, pour les voitures autonomes, l'image contiendrait la route, les voitures, les piétons, etc. Nous pourrions donc avoir besoin d'utiliser la segmentation ici pour séparer les objets et analyser chaque objet individuellement (c'est-à-dire la classification de l'image) pour vérifier de quoi il s'agit.

Dans cet exercice, Vous réaliserez une application Streamlit qui permet de charger une image puis affiche le résultat de la segmentation d'image avec une méthode d’apprentissage non-supervisé qui est le clustering K-Means, et ce, en faisant varier le nombre de clusters K via l’interface. 

N.B. : Dans cette application, chaque pixel de l’image est considéré comme une observation.
