import requests

GROK_API_KEY = "gsk_ZwYRitVAEcSFFXZgfhSRaC5tWGdyb3FYqbgAb6CAm68JvyG20ZlZf3AIXYYYXX"

def generate_answer(query):
    url = "https://api.x.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "grok-2-mini",   # ✅ working model try this
        "messages": [
            {"role": "user", "content": query}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        res = response.json()

        print("DEBUG:", res)

        if "choices" in res:
            return res["choices"][0]["message"]["content"]
        else:
            return f"⚠️ API Error: {res}"

    except Exception as e:
        return f"❌ Error: {str(e)}"
