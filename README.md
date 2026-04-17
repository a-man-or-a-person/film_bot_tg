# Film Bot Telegram

## Introduction
This project is a Telegram bot designed to assist users in discovering and managing their film watching experience. It provides users with film recommendations, information about films, and allows users to track their watched films.

## Features
- Film recommendations based on user preferences.
- Search functionality for films and TV shows.
- Track watched films and manage lists.
- User-friendly interface with quick commands.
- Logging for tracking user interactions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/a-man-or-a-person/film_bot_tg.git
   ```
2. Navigate to the project directory:
   ```bash
   cd film_bot_tg
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables as needed.

## Usage
- Start the bot by running:
   ```bash
   python bot.py
   ```
- Interact with the bot through your Telegram application using the command `/start` to initiate the conversation.

## Architecture
The project follows a modular architecture, separating the command handling, API communication, and database interactions into individual modules. This promotes clear separation of concerns and easier maintenance.

## Technologies
- Python 3.x
- [Python Telegram Bot](https://python-telegram-bot.readthedocs.io/)
- SQLAlchemy for database management
- Requests for API interactions

## Database Schema
The database stores user interactions, film data, and user preferences in structured tables. Ensure the database is initialized before running the bot.
