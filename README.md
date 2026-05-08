# 🏎️ F1 Predictor Bot - 2026 Season

An automated Discord bot to manage Formula 1 predictions within your community.
Users can predict Grand Prix results, earn points, and climb a fully automated leaderboard.

---

# ✨ Features

## 🎯 Complete Predictions via Slash Commands
- Use of Discord `/` commands for a smooth experience.
- Reduction of input errors.
- Clear and intuitive interface.

## 🤖 Automation of Results
- Automatic retrieval of official results via the Jolpi API.
- Management of:
  - Race Top 10
  - Qualifications
  - DNF
  - Special bonuses

## 🧮 Advanced Point System
- Multipliers based on the exact predicted position.
- The higher the position, the higher the points earned.
- Bonuses:
  - Driver of the Day
  - Safety Car
  - Number of overtakes
  - Special bets

## 🛡️ Secure Administrative Management
Commands reserved according to Discord roles. For our discord:
- 🔱 Streamer
- 🏴‍☠️ Patron
- 🔧 Moderator

Admin features:
- Result validation
- Score correction
- Event management

## 🏆 Dynamic Leaderboard
- Leaderboard updated automatically.
- Display of the best players of the weekend.
- Automatic mentions of the winners.

---

# 🛠️ Installation

## 📋 Prerequisites

- Python 3.8+
- A Discord bot created on the Discord Developer Portal

---

# 🚀 Project Configuration

## 1️⃣ Clone the Repository

```bash
git clone [https://github.com/votre-utilisateur/F1_predictor_bot.git](https://github.com/votre-utilisateur/F1_predictor_bot.git)
cd F1_predictor_bot
```

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Activating the Environment

#### Windows
```bash
.\venv\Scripts\activate
```

#### Linux / macOS
```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

## Create a `.env` File

At the root of the project:

```env
TOKEN=YOUR_DISCORD_BOT_TOKEN
ADMIN_ROLE1=YOUR_DISCORD_ADMIN_ROLE_ID

# If you only have one admin role, you can delete the values below.
# However, don't forget to remove the corresponding lines in predict_f1 lines 22, 23, and 25.
ADMIN_ROLE2=YOUR_DISCORD_ADMIN_ROLE_ID
ADMIN_ROLE3=YOUR_DISCORD_ADMIN_ROLE_ID
```

---

## 🔑 Permissions and Roles

The authorized role IDs are configured directly in:

```plaintext
src/predict_f1.py
```

Supported roles for our Discord:
- 🔱 Streamer
- 🏴‍☠️ Patron
- 🔧 Moderator

---

# 📚 Development Standards

The project follows these conventions:
- PEP 8
- Pythonic programming
- Maintainable and readable code

---

# 🧼 Applied Best Practices

## ✍️ Readability & Style (PEP 8)

- Single TAB indentation
- Consistent spacing around operators
- Lines limited to 79 characters
- Clean and structured line breaks

---

## 🏷️ Naming Conventions

### Variables and functions
```python
resultats_reels
```

### Global constants
```python
API_BASE
```

### Classes
```python
F1Bot
```

---

# 📖 Documentation

Each module contains:
- Docstrings
- Explanations of arguments
- Return values

---

# 🛡️ Code Robustness

## Proper Error Handling
- Use of targeted `try-except` blocks
- No bare `except:`
- Consistent returns (explicit `None` if necessary)

## Import Organization
Respected order:
1. Standard libraries
2. Third-party libraries
3. Local modules

---

# 📂 Project Architecture

```plaintext
F1_predictor_bot/
├── data/               # JSON storage (predictions, scores)
├── src/
│   ├── api_f1.py       # Jolpi API calls
│   ├── data_manager.py # Data management
│   └── predict_f1.py   # Main Discord bot
├── .env                # Environment variables
├── .gitignore          # Git exclusions
└── README.md           # Documentation
```

---

# 📦 Main Dependencies

- discord.py
- requests
- python-dotenv

---

# 🌐 API Used

## Jolpi API
Allows retrieving:
- Grand Prix results
- Qualifications
- Rankings
- Driver information

---

# 🚧 Future Features

- Admin Web Interface
- SQL Database
- Full season history
- Advanced statistics
- Multi-server support

---

# 🤝 Contribution

Contributions are welcome. Please contact me by email to join the Git repo.

## Recommended Workflow

```bash
git checkout -b feature/my-feature
git commit -m "feat(function): Add new feature"
git push origin feature/my-feature
```

Then open a Pull Request.

---

# 📜 License

Project under MIT license.

---

# 👤 Author

QUIATOL Evan

# 👥 Ideas by:

CNC-Liam (discord: _liamgamer) and QUIATOL Evan