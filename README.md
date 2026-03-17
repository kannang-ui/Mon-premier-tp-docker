# 🚀 Compteur de Visites - Architecture Docker Sécurisée

Ce projet démontre la mise en place d'une infrastructure conteneurisée complète utilisant **Docker** et **Docker Compose**. Il simule une application réelle avec un frontend Python et une base de données de persistance.

## 🏗️ Architecture du Projet
L'application est découpée en deux services distincts :
- **Web** : Application Flask (Python) gérant l'interface utilisateur.
- **Database** : Instance Redis (Alpine) pour le stockage des visites.

## 🛡️ Points Clés Techniques
- **Persistance** : Utilisation de volumes Docker pour conserver les données de Redis même après l'arrêt des conteneurs.
- **Sécurité** : Authentification forcée sur Redis via mot de passe.
- **Gestion de l'environnement** : Isolation des secrets et configurations dans un fichier `.env` (non versionné).
- **Hygiène Docker** : Optimisation des images (utilisation de versions Alpine) pour réduire l'empreinte disque.

## 🚀 Installation et Lancement

1. **Cloner le dépôt** :
   ```bash
   git clone <url-de-ton-depot>
   cd <nom-du-dossier>