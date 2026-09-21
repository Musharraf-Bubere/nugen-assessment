import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NUGEN_API_KEY")

URL = "https://api.nugen.in/api/v3/inference/chat/completions"

MODEL_ID = "model_01m31y707yfnxsh0"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


def ask_nugen(question):
    payload = {
        "model": MODEL_ID,
        "messages": [
            {
                "role": "user",
                "content": question,
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

    if response.status_code != 200:
        raise Exception(f"Nugen API Error: {data}")

    return {
        "answer": data["choices"][0]["message"]["content"],
        "confidence": data.get("confidence_score"),
        "usage": data.get("usage", {}),
    }


def main():
    print("=" * 60)
    print("Nugen AI Knowledge Assistant")
    print("=" * 60)

    question = input("\nAsk a question: ")

    result = ask_nugen(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nConfidence Score:", result["confidence"])

    usage = result["usage"]

    print("\nToken Usage:")
    print("Prompt Tokens:", usage.get("prompt_tokens"))
    print("Completion Tokens:", usage.get("completion_tokens"))
    print("Total Tokens:", usage.get("total_tokens"))


if __name__ == "__main__":
    main()