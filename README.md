# Daily Govt Exam Telegram Quiz Bot

Automated Telegram Bot pipeline that generates and posts 10 interactive quiz questions daily to a Telegram Channel at **5:00 PM IST**.

## Folder Structure
- `quiz_bot.py`: Main executable script that reads questions, prevents repetition, and posts native Telegram Quiz Polls (`sendPoll` with `type="quiz"`).
- `config.json`: Configuration storing your `bot_token` and `channel_id`.
- `questions_bank.json`: Bank of high-yield questions covering all government exam subjects.
- `quiz_history.json`: Automatically tracks sent question IDs to ensure zero duplicate quizzes.

## Telegram Setup (2 Minutes)

### 1. Create Telegram Bot
1. Open Telegram and search for `@BotFather`.
2. Send `/newbot`.
3. Give your bot a name (e.g. `Govt Exam Daily Quiz`) and a username ending in `bot` (e.g. `GovtExamDailyQuizBot`).
4. Copy the API Token (e.g. `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`).

### 2. Connect Your Channel
1. Open your Telegram Channel (or create a new Public/Private Channel).
2. Go to **Channel Settings** > **Administrators** > **Add Administrator**.
3. Search for your bot username and add it as an **Admin** with permission to **Post Messages**.
4. Note your Channel Username (e.g., `@MyGovtExamQuizChannel`) or numeric Chat ID.

### 3. Update `config.json`
Open `config.json` and enter your details:
```json
{
  "bot_token": "YOUR_ACTUAL_BOT_TOKEN_FROM_BOTFATHER",
  "channel_id": "@YourChannelUsername",
  "is_anonymous": false
}
```

### 4. Test Live Run
```bash
python quiz_bot.py
```
Or test in simulation mode without sending:
```bash
python quiz_bot.py --dry-run
```
