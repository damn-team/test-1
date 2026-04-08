import requests

API_KEY = "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"

url = "https://integrate.api.nvidia.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("🤖 AI Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Exiting chatbot...")
        break

    payload = {
        "model": "meta/llama-3.1-8b-instruct",
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            print("\nAI:", reply, "\n")
        else:
            print("❌ Error:", response.status_code, response.text)

    except Exception as e:
        print("⚠️ Exception:", str(e))