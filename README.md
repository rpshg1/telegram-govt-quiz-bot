# Daily Govt Exam Telegram Quiz Bot

Automated Telegram Bot pipeline that generates and posts 10 interactive quiz questions daily to a Telegram Channel at **5:00 PM IST**.

## Folder Structure
- `quiz_bot.py`: Main executable script that reads questions, prevents repetition, and posts native Telegram Quiz Polls (`sendPoll` with `type="quiz"`).
- `config.example.json`: Example template for local configuration (copy to `config.json`).
- `questions_bank.json`: Bank of 6,700+ high-yield questions covering all government exam subjects.
- `quiz_history.json`: Automatically tracks sent question IDs and session slots to ensure zero duplicate quizzes.

## Telegram Setup

### 1. Create Telegram Bot
1. Open Telegram and search for `@BotFather`.
2. Send `/newbot`.
3. Give your bot a display name and username ending in `bot`.
4. Copy the API Token (e.g. `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`).

### 2. Connect Your Channel
1. Open your Telegram Channel (Public or Private).
2. Go to **Channel Settings** > **Administrators** > **Add Administrator**.
3. Search for your bot username and add it as an **Admin** with permission to **Post Messages**.
4. Note your Channel Username (e.g., `@MyGovtExamQuizChannel`).

### 3. Local Setup (Optional)
Copy `config.example.json` to `config.json` (this file is gitignored and will never be pushed to GitHub):
```json
{
  "bot_token": "YOUR_ACTUAL_BOT_TOKEN_FROM_BOTFATHER",
  "channel_id": "@YourChannelUsername",
  "is_anonymous": true
}
```

### 4. GitHub Actions Setup (Cloud Automated)
In your GitHub Repository, go to **Settings** > **Secrets and variables** > **Actions** and add:
- `TELEGRAM_BOT_TOKEN`: Your bot token from `@BotFather`.
- `TELEGRAM_CHANNEL_ID`: Your channel username (e.g. `@YourChannelUsername`).

### 4. Test Live Run
```bash
python quiz_bot.py
```
Or test in simulation mode without sending:
```bash
python quiz_bot.py --dry-run
```
