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

### Running the Application

1. **Start the Flask server**:
   ```bash
   python atm.py
   ```

2. **Access the app**:
   Open your browser and navigate to `http://127.0.0.1:5000`

## 🔑 Demo Credentials

- **Account Number**: `12345678`
- **PIN**: `1234`

## 📂 Project Structure

```text
├── static/          # CSS, JS, and image assets
├── templates/       # HTML view templates
├── atm.py           # Core application logic
├── requirements.txt # Project dependencies
├── .env.example     # Environment variable template
└── .gitignore       # Git exclusion rules
```

## 🔒 Security Note

The `atm.db` file and `.env` file are excluded from the repository to prevent leaking sensitive data or user information. Always use unique secret keys in production environments.

---

*Developed with ❤️ for the community.*
