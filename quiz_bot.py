import os
import sys
import json
import time
import random
from typing import List, Dict, Any
import requests

# Fix Windows console UTF-8 output
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "quiz_history.json")
QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), "questions_bank.json")

def load_config() -> Dict[str, Any]:
    env_token = os.getenv("TELEGRAM_BOT_TOKEN")
    env_channel = os.getenv("TELEGRAM_CHANNEL_ID")
    if env_token and env_channel:
        return {
            "bot_token": env_token,
            "channel_id": env_channel,
            "is_anonymous": True
        }
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            if env_token:
                cfg["bot_token"] = env_token
            if env_channel:
                cfg["channel_id"] = env_channel
            return cfg
    return {
        "bot_token": env_token or "",
        "channel_id": env_channel or "",
        "is_anonymous": True
    }

def save_config(bot_token: str, channel_id: str, is_anonymous: bool = True):
    config = {
        "bot_token": bot_token,
        "channel_id": channel_id,
        "is_anonymous": is_anonymous
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

def load_history() -> List[int]:
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("sent_ids", [])
    return []

def save_history(sent_ids: List[int]):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump({"sent_ids": sent_ids, "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")}, f, indent=2)

def send_telegram_quiz(bot_token: str, channel_id: str, question_data: Dict[str, Any], is_anonymous: bool = False) -> bool:
    """
    Sends a native Telegram Quiz Poll to the specified channel.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendPoll"
    payload = {
        "chat_id": channel_id,
        "question": question_data["question"],
        "options": json.dumps(question_data["options"]),
        "type": "quiz",
        "correct_option_id": int(question_data["correct_option_id"]),
        "explanation": question_data.get("explanation", ""),
        "is_anonymous": is_anonymous
    }

    try:
        response = requests.post(url, data=payload, timeout=15)
        res_json = response.json()
        if res_json.get("ok"):
            print(f"[SUCCESS] Sent Quiz: {question_data['question'][:50]}...")
            return True
        else:
            print(f"[ERROR] Telegram API Error: {res_json.get('description')}")
            return False
    except Exception as e:
        print(f"[EXCEPTION] Failed to send poll: {e}")
        return False

def get_10_daily_questions() -> List[Dict[str, Any]]:
    """Select 10 balanced questions across all government exam subjects."""
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        all_questions = json.load(f)

    sent_ids = set(load_history())
    
    # Filter out already sent questions
    available = [q for q in all_questions if q["id"] not in sent_ids]
    
    # If we ran out of questions, reset history
    if len(available) < 10:
        print("[INFO] Question pool exhausted. Resetting history for fresh rotation...")
        sent_ids = set()
        available = all_questions

    # Group by subject to ensure all subjects are covered
    by_subject = {}
    for q in available:
        subj = q.get("subject", "General Knowledge")
        by_subject.setdefault(subj, []).append(q)

    selected = []
    # Pick 1 from each subject category first
    subjects = list(by_subject.keys())
    random.shuffle(subjects)
    
    for subj in subjects:
        if len(selected) >= 10:
            break
        if by_subject[subj]:
            chosen = random.choice(by_subject[subj])
            selected.append(chosen)
            by_subject[subj].remove(chosen)

    # Fill remainder if less than 10
    remaining = [q for q in available if q not in selected]
    random.shuffle(remaining)
    while len(selected) < 10 and remaining:
        selected.append(remaining.pop())

    return selected

def run_daily_quiz_pipeline(dry_run: bool = False):
    config = load_config()
    bot_token = config.get("bot_token")
    channel_id = config.get("channel_id")
    is_anonymous = config.get("is_anonymous", True)

    if not dry_run:
        if not bot_token or bot_token == "YOUR_TELEGRAM_BOT_TOKEN":
            print("[ERROR] Telegram Bot Token is not configured. Please edit config.json.")
            return False
        if not channel_id or channel_id == "@your_channel_username":
            print("[ERROR] Telegram Channel ID is not configured. Please edit config.json.")
            return False

    print("==================================================")
    print("  Daily Govt Exam Quiz - Telegram Bot Pipeline    ")
    print("==================================================")
    print(f"Target Channel : {channel_id if not dry_run else 'DRY-RUN (Simulated)'}")
    print(f"Total Quizzes  : 10 Questions")
    print("--------------------------------------------------")

    questions = get_10_daily_questions()
    sent_ids = load_history()
    success_count = 0

    for i, q in enumerate(questions, start=1):
        print(f"\n[Q{i}/10] [{q.get('subject', 'GK')}] {q['question']}")
        for opt_idx, opt in enumerate(q['options']):
            marker = "*" if opt_idx == q['correct_option_id'] else " "
            print(f"  {marker} ({chr(65+opt_idx)}) {opt}")
        print(f"  Explanation: {q.get('explanation')}")

        if dry_run:
            success_count += 1
            sent_ids.append(q["id"])
        else:
            success = send_telegram_quiz(bot_token, channel_id, q, is_anonymous)
            if success:
                success_count += 1
                sent_ids.append(q["id"])
            time.sleep(2)  # Avoid rate limit

    save_history(sent_ids)
    print("\n--------------------------------------------------")
    print(f"Completed! {success_count}/10 Quizzes sent successfully.")
    print("==================================================")
    return success_count == 10

if __name__ == "__main__":
    import sys
    is_dry = "--dry-run" in sys.argv
    run_daily_quiz_pipeline(dry_run=is_dry)
