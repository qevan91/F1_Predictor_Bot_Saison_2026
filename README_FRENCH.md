# 🏎️ F1 Predictor Bot - Saison 2026

Un bot Discord automatisé pour gérer les pronostics de Formule 1 au sein de votre communauté.  
Les utilisateurs peuvent prédire les résultats des Grands Prix, gagner des points et grimper dans un classement entièrement automatisé.

---

# ✨ Fonctionnalités

## 🎯 Pronostics complets via Slash Commands
- Utilisation des commandes `/` Discord pour une expérience fluide.
- Réduction des erreurs de saisie.
- Interface claire et intuitive.

## 🤖 Automatisation des résultats
- Récupération automatique des résultats officiels via l’API Jolpi.
- Gestion :
  - Top 10 course
  - Qualifications
  - DNF
  - Bonus spéciaux

## 🧮 Système de points avancé
- Multiplicateurs selon la position exacte prédite.
- Plus la position est haute, plus les points gagnés sont élevés.
- Bonus :
  - Driver of the Day
  - Safety Car
  - Nombre de dépassements
  - Paris spéciaux

## 🛡️ Gestion administrative sécurisée
Commandes réservées selon les rôles Discord. Pour notre discord :
- 🔱 Streamer
- 🏴‍☠️ Patron
- 🔧 Modérateur

Fonctionnalités admin :
- Validation des résultats
- Correction des scores
- Gestion des événements

## 🏆 Classement dynamique
- Leaderboard mis à jour automatiquement.
- Affichage des meilleurs joueurs du week-end.
- Mentions automatiques des gagnants.

---

# 🛠️ Installation

## 📋 Prérequis

- Python 3.8+
- Un bot Discord créé sur le Discord Developer Portal

---

# 🚀 Configuration du projet

## 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/F1_predictor_bot.git
cd F1_predictor_bot
```

## 2️⃣ Créer un environnement virtuel

```bash
python -m venv venv
```

### Activation de l’environnement

#### Windows
```bash
.\venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

## 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

## Créer un fichier `.env`

À la racine du projet :

```env
TOKEN=YOUR_DISCORD_BOT_TOKEN
ADMIN_ROLE1=YOUR_DISCORD_ADMIN_ROLE_ID

# Si vous n'avez qu'un seul rôle admin, Vous pouvez supprimer les valeurs si dessous.
# Cependant n'oubliez pas d'enlever les correspondances dans predict_f1 lignes 22, 23 et 25.
ADMIN_ROLE2=YOUR_DISCORD_ADMIN_ROLE_ID
ADMIN_ROLE3=YOUR_DISCORD_ADMIN_ROLE_ID
```

---

## 🔑 Permissions et rôles

Les IDs des rôles autorisés sont configurés directement dans :

```plaintext
src/predict_f1.py
```

Rôles supportés pour notre Discord :
- 🔱 Streamer
- 🏴‍☠️ Patron
- 🔧 Modérateur

---

# 📚 Standards de Développement

Le projet suit les conventions :
- PEP 8
- Programmation Pythonique
- Code maintenable et lisible

---

# 🧼 Bonnes pratiques appliquées

## ✍️ Lisibilité & Style (PEP 8)

- Indentation d'un seul TAB
- Espaces cohérents autour des opérateurs
- Lignes limitées à 79 caractères
- Sauts de lignes propres et structurés

---

## 🏷️ Conventions de nommage

### Variables et fonctions
```python
resultats_reels
```

### Constantes globales
```python
API_BASE
```

### Classes
```python
F1Bot
```

---

# 📖 Documentation

Chaque module contient :
- Des docstrings
- Des explications des arguments
- Les valeurs de retour

---

# 🛡️ Robustesse du code

## Gestion propre des erreurs
- Utilisation de `try-except` ciblés
- Aucun `except:` nu
- Retours cohérents (`None` explicite si nécessaire)

## Organisation des imports
Ordre respecté :
1. Librairies standard
2. Librairies tierces
3. Modules locaux

---

# 📂 Architecture du Projet

```plaintext
F1_predictor_bot/
├── data/               # Stockage JSON (predictions, scores)
├── src/
│   ├── api_f1.py       # Appels API Jolpi
│   ├── data_manager.py # Gestion des données
│   └── predict_f1.py   # Bot Discord principal
├── .env                # Variables d'environnement
├── .gitignore          # Exclusions Git
└── README.md           # Documentation
```

---

# 📦 Dépendances principales

- discord.py
- requests
- python-dotenv

---

# 🌐 API utilisée

## Jolpi API
Permet de récupérer :
- Résultats des Grands Prix
- Qualifications
- Classements
- Informations pilotes

---

# 🚧 Fonctionnalités futures

- Interface Web Admin
- Base de données SQL
- Historique complet des saisons
- Statistiques avancées
- Support multi-serveurs

---

# 🤝 Contribution

Les contributions sont les bienvenues. Merci de me contacter par mail pour entrer dans le répo Git.

## Workflow conseillé

```bash
git checkout -b feature/ma-feature
git commit -m "feat(fonction): Ajout nouvelle fonctionnalité"
git push origin feature/ma-feature
```

Puis ouvrir une Pull Request.

---

# 📜 Licence

Projet sous licence MIT.

---

# 👤 Auteur

QUIATOL Evan

# 👥 Idées de :

CNC-Liam (discord : _liamgamer) et QUIATOL Evan 