import requests

def get_answer_from_blackbox(question):
    url = "https://www.blackbox.ai/api/chat"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "AI-Study-Helper"
    }
    data = {
        "messages": [
            {"role": "user", "content": question}
        ],
        "model": "gpt-3.5-turbo"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("📘 Welcome to AI Study Helper!")
    while True:
        question = input("\nAsk your study question (or type 'exit'): ")
        if question.lower() == "exit":
            break
        answer = get_answer_from_blackbox(question)
        print("\n🧠 Answer:", answer)
