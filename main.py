import os
from dotenv import load_dotenv

from tools.browser import collect_page_data
from agents.tester_agent import analyze_with_ai

load_dotenv()

DEFAULT_URL = os.getenv("DEFAULT_URL")


def run_test(url=None):
    os.makedirs("reports", exist_ok=True)

    # ✅ FIX: fallback to .env
    if not url:
        url = DEFAULT_URL

    print(f"➡️ Testing: {url}")  # ✅ debug

    print("➡️ Collecting data...")
    data = collect_page_data(url)

    print("➡️ Running AI agent...")
    findings = analyze_with_ai(data)

    with open("reports/findings.json", "w") as f:
        f.write(str(findings))

    print("✅ Done!")