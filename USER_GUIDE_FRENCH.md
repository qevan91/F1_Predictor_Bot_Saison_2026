# 📖 Guide de l'Utilisateur - F1 Predictor 2026

Bienvenue dans le guide officiel du bot **F1 Predictor** ! Ce document explique comment participer, comment les points sont calculés et comment les administrateurs gèrent les courses.

## 🏎️ Pour les Joueurs

### 🏁 1. Faire son pronostic
La commande principale est `/prono`. Une fois lancée, un formulaire s'affiche. Tu dois remplir les champs suivants :
- **Qualifications (Top 3) :** Qui sera en Pole, 2ème et 3ème ?
- **Course (Top 10) :** Tes prédictions pour les 10 premières places.
- **Meilleure Équipe :** L'écurie qui marquera le plus de points selon toi.
- **Voiture de Sécurité :** Vrai ou Faux ?
- **Abandons :** Le nombre total de voitures qui ne finiront pas et leurs noms.
- **Bonus :** Le Pilote du Jour (vote des fans) et celui qui fera le plus de dépassements.

> **Note :** Tu peux modifier ton prono autant de fois que tu veux avant le début des qualifications. Seul le dernier envoi compte !

### 📊 2. Consulter le Classement
Utilise `/classement` pour voir qui domine la saison. Le bot affiche le total de points cumulés de chaque joueur avec des médailles pour le podium.

### 📅 3. Infos du Grand Prix
Utilise `/prochain_gp` pour connaître les horaires et le circuit du prochain week-end de course.

---

## 🏆 Le Système de Points

Le barème est conçu pour récompenser la précision :

| Type de pari | Position exacte | Présent mais mal placé |
| :--- | :--- | :--- |
| **Qualifications (Top 3)** | **8 pts (P1)** / **7 pts (P2)** / **6 pts (P3)** | +2 pts |
| **Course (Top 10)** | **15 pts (P1)** dégressif jusqu'à **6 pts (P10)** | +2 pts |
| **Meilleure Équipe** | **+5 pts** | - |
| **Voiture de Sécurité** | **+2 pts** | - |
| **Nombre d'abandons** | **+3 pts** | - |
| **Nom d'un pilote DNF** | **+2 pts** par pilote trouvé | - |
| **Pilote du Jour / Dépassements** | **+5 pts** | - |

---

## 🛡️ Pour les Administrateurs

Les commandes suivantes sont réservées aux rôles **Streamer, Patron et Modérateur**.

1. **`/auto_resultats` :** À utiliser après la course. Le bot va chercher tout seul le Top 10, le Top 3 Qualif et les abandons. Tu n'as qu'à saisir la Safety Car, le Pilote du jour et les dépassements.
2. **`/resultats_manuels` :** Si l'API est en panne, utilise cette commande pour tout saisir à la main.
3. **`/reset_pronos` :** **Obligatoire** avant chaque nouveau Grand Prix pour vider les paris du week-end précédent.
4. **`/modifier_score` :** Pour ajouter ou retirer des points manuellement (pénalités, disqualifications après-course, etc.).