import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_story(news_blob: str) -> str:
    if not news_blob.strip():
        return "No news available to generate story."

    prompt = f"""
You are a professional news analyst briefing a CEO. 

Here are today's headlines and summaries:

{news_blob}

Instructions:
1. Transform these into a cohesive, flowing narrative.
2. Stick strictly to the facts; do not add personal opinions or speculation.
3. For each story, provide one clear, concise implication for business, economy, or policy.
4. Group stories by theme: 🌍 Geopolitics & Policy, 📊 Economy & Markets, 💻 Technology & Industry, 🌱 Social/Environment.
5. Use emojis to highlight each section.
6. End with a quirky fun fact and a Thought of the Day.
7. Total output should be roughly 1000 words (~15 min read).
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        result = response.json()

       
        story_text = result.get("response") or result.get("text") or ""
        return story_text.strip() if story_text else "No story generated."

    except requests.exceptions.RequestException as e:
        return f"❌ Ollama request error: {e}"

    except Exception as e:
        return f"❌ Unexpected error: {e}"
