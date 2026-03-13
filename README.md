# 🛡️ SecurityBot

A robust Discord bot built with **Python** and **discord.py**. This project is designed to enhance server security while providing fun utility features for community engagement.

## 🌟 Key Features

### 🔐 Security & Moderation
* **Security Alerts:** Monitors server activity and provides real-time alerts for administrators.
* **Admin Lockdown:** Features specialized commands restricted to the bot owner/admin to prevent unauthorized access.
* **Modular Design:** Built using `Cogs`, making it easy to add or remove security modules without affecting the core bot.

### 🎮 Utility & Fun
* **Automated Messaging:** Periodically sends random messages from a curated list.
* **Spam Management:** Custom tools to control or stop automated messaging tasks.
* **Slash Commands:** Fully supports modern Discord Slash Commands for an intuitive user experience.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Library:** [discord.py](https://github.com/Rapptz/discord.py)
* **Configuration:** `python-dotenv` for secure environment variable management.

---

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/husekrichard4321-glitch/SecurityBot.git](https://github.com/husekrichard4321-glitch/SecurityBot.git)
    cd SecurityBot
    ```

2.  **Install dependencies:**
    ```bash
    pip install discord.py python-dotenv
    ```

3.  **Environment Setup:**
    Create a `.env` file in the root directory and add your Discord token:
    ```text
    DISCORD_TOKEN=your_token_here
    ```

4.  **Run the bot:**
    ```bash
    python main.py
    ```

---

## 📂 Project Structure
```text
SecurityBot/
├── cogs/                # Modular command categories
│   ├── fun_utility.py   # Messaging and fun tools
│   └── security.py      # Security and alert systems
├── main.py              # Main entry point and bot setup
├── .env                 # Secret keys (ignored by Git)
├── .gitignore           # Tells Git which files to ignore
└── README.md            # Project documentation