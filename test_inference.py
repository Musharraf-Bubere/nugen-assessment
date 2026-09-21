import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NUGEN_API_KEY")

URL = "https://api.nugen.in/api/v3/inference/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

with open("evaluation_questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

for item in questions:
    payload = {
        "model": "model_01m31y707yfnxsh0",
        "messages": [
            {
                "role": "user",
                "content": item["question"],
            }
        ],
        "max_tokens": 500,
        "temperature": 0.2,
        "stream": False,
    }

    response = requests.post(
        URL,
        headers=headers,
        json=payload,
    )

    data = response.json()

    print("=" * 80)
    print(f"{item['id']} - {item['category']}")
    print(f"Question: {item['question']}")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        answer = data["choices"][0]["message"]["content"]
        confidence = data.get("confidence_score")
        usage = data.get("usage", {})

        print("\nAnswer:")
        print(answer)

        print(f"\nConfidence Score: {confidence}")

        print("\nToken Usage:")
        print(f"Prompt Tokens: {usage.get('prompt_tokens')}")
        print(f"Completion Tokens: {usage.get('completion_tokens')}")
        print(f"Total Tokens: {usage.get('total_tokens')}")

    else:
        print("\nError:")
        print(data)