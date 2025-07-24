import os
import requests
from datetime import datetime, timezone

# ─── CONFIG ────────────────────────────────────────────────
TARGET = datetime(2026, 2, 1, tzinfo=timezone.utc)   # GATE exam date
ROLE_ID = "1397557995436638208"                      # @GATE
# ─────────────────────────────────────────────────────────

now  = datetime.now(timezone.utc)
days = max((TARGET - now).days, 0)

embed = {
    "title":       "⏳ Countdown to GATE Exam",
    "description": (
        f"Only **{days}** day{'s' if days != 1 else ''} left until 📅 **2026‑02‑01**!\n"
        f"<@&{ROLE_ID}>"
    ),
    "color":       int("f600ff", 16),
    "fields": [
        {
            "name":  "💪 Daily Motivation",
            "value": "Keep pushing—every problem you solve today brings you one step closer to your goal."
        }
    ],
    "footer": {"text": "Auto‑updated via GitHub Actions"},
    "timestamp": now.isoformat()
}

resp = requests.post(os.environ["DISCORD_WEBHOOK_URL"], json={"embeds":[embed]})
resp.raise_for_status()
