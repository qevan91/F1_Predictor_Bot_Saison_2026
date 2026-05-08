# 📖 User Guide - F1 Predictor 2026

Welcome to the official **F1 Predictor** bot guide! This document explains how to participate, how points are calculated, and how administrators manage the races.

## 🏎️ For Players

### 🏁 1. Making a Prediction
The main command is `/prono`. Once launched, a form will appear. You must fill in the following fields:
- **Qualifications (Top 3):** Who will be on Pole, 2nd, and 3rd?
- **Race (Top 10):** Your predictions for the top 10 positions.
- **Best Team:** The constructor that will score the most points in your opinion.
- **Safety Car:** True or False?
- **Retirements (DNF):** The total number of cars that will not finish and their names.
- **Bonus:** Driver of the Day (fan vote) and the driver with the most overtakes.

> **Note:** You can modify your prediction as many times as you want before the start of qualifying. Only the last submission counts!

### 📊 2. Checking the Ranking
Use `/classement` to see who is dominating the season. The bot displays the total cumulative points for each player with medals for the podium.

### 📅 3. Grand Prix Info
Use `/prochain_gp` to find out the schedule and circuit for the next race weekend.

---

## 🏆 Point System

The scoring system is designed to reward precision:

| Bet Type | Exact Position | Present but wrong place |
| :--- | :--- | :--- |
| **Qualifications (Top 3)** | **8 pts (P1)** / **7 pts (P2)** / **6 pts (P3)** | +2 pts |
| **Race (Top 10)** | **15 pts (P1)** decreasing to **6 pts (P10)** | +2 pts |
| **Best Team** | **+5 pts** | - |
| **Safety Car** | **+2 pts** | - |
| **Number of DNFs** | **+3 pts** | - |
| **DNF Driver Name** | **+2 pts** per driver found | - |
| **Driver of the Day / Overtakes** | **+5 pts** | - |

---

## 🛡️ For Administrators

The following commands are reserved for the **Streamer, Patron, and Moderator** roles.

1. **`/auto_resultats`:** To be used after the race. The bot will automatically fetch the Top 10, Top 3 Quali, and DNFs. You only need to enter the Safety Car, Driver of the Day, and overtakes.
2. **`/resultats_manuels`:** If the API is down, use this command to enter everything manually.
3. **`/reset_pronos`:** **Mandatory** before each new Grand Prix to clear the bets from the previous weekend.
4. **`/modifier_score`:** To manually add or remove points (penalties, post-race disqualifications, etc.).