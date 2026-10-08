import os
from openai import OpenAI

LOG_FILE = "app/application.log"

client = OpenAI()


def read_logs():
    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return None

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        return file.read()


def analyze_logs(logs):
    prompt = f"""
You are an AI DevOps assistant.

Analyze the following application logs.

Identify:
1. The most important error
2. Severity: LOW, MEDIUM, HIGH, or CRITICAL
3. Root cause
4. Recommended solution

Do not suggest dangerous automatic actions.
A human DevOps engineer should verify the recommendation.

Application logs:
{logs}
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text


if __name__ == "__main__":
    logs = read_logs()

    if logs:
        print("===== AI DEVOPS ANALYSIS =====")
        result = analyze_logs(logs)
        print(result)