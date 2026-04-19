# 🏦 ATM Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)

A professional, feature-rich ATM Management System built with **Flask** and **SQLite**. This application simulates a real-world ATM experience with a modern, responsive web interface.

## ✨ Key Features

- 🔐 **Secure Authentication**: Access accounts using unique account numbers and PINs.
- 💰 **Financial Operations**: Perform deposits and withdrawals with real-time balance updates.
- 📊 **Transaction History**: Comprehensive log of all activities, including a mini-statement dashboard.
- 📱 **Responsive Design**: Fully optimized for both desktop and mobile devices.
- 🛡️ **Security Focused**: Environment variable support for secret keys and gitignored database files.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript
- **Environment Management**: Python-dotenv

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/atm-management-system.git
   cd atm-management-system
   ```

2. **Create a virtual environment** (Recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Copy `.env.example` to a new file named `.env` and update the values:
   ```bash
   cp .env.example .env
   ```
   *Edit `.env` and set a secure `FLASK_SECRET_KEY`.*

### Deployment (Render.com)

1.  **Create an account** on [Render.com](https://render.com).
2.  **Dashboard** > **New** > **Web Service**.
3.  Connect your GitHub repository.
4.  Render will automatically detect the settings from `render.yaml`.
5.  **Environment Variables**:
    *   Add `DATABASE_URL`: Your Supabase connection string.
    *   Add `FLASK_SECRET_KEY`: A secure random password.
6.  Click **Deploy**.

## 🔑 Demo Credentials

- **Account Number**: `12345678`
- **PIN**: `1234`

## 📂 Project Structure

```text
├── static/          # CSS, JS, and image assets
├── templates/       # HTML view templates
├── atm.py           # Core application logic
├── requirements.txt # Project dependencies
├── render.yaml      # Render deployment config
└── .gitignore       # Git exclusion rules
```

## 🔒 Security Note

The `atm.db` file and `.env` file are excluded from the repository. In production, the app uses **Supabase (PostgreSQL)** for persistence.

---

*Developed with ❤️ for the community.*
