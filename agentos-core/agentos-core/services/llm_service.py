
import os
import openai
import anthropic
import requests

# Carregar chaves e provedores do .env
LLM_1 = os.getenv("LLM_PROVIDER", "openai")
LLM_1_KEY = os.getenv("LLM_API_KEY", "")
LLM_2 = os.getenv("LLM_SECONDARY_PROVIDER", "anthropic")
LLM_2_KEY = os.getenv("LLM_SECONDARY_API_KEY", "")
LLM_3 = os.getenv("LLM_TERTIARY_PROVIDER", "mistral")
LLM_3_KEY = os.getenv("LLM_TERTIARY_API_KEY", "")
LLM_3_ENDPOINT = os.getenv("LLM_TERTIARY_API_URL", "https://api.fireworks.ai/inference/v1/chat/completions")

# Inicializar clientes
openai.api_key = LLM_1_KEY
anthropic.api_key = LLM_2_KEY

def call_openai(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model=os.getenv("LLM_MODEL", "gpt-4"),
        messages=[{"role": "user", "content": prompt}],
        timeout=30
    )
    return response.choices[0].message.content.strip()

def call_anthropic(prompt: str) -> str:
    client = anthropic.Anthropic(api_key=LLM_2_KEY)
    response = client.messages.create(
        model=os.getenv("LLM_2_MODEL", "claude-3-opus-20240229"),
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text.strip()

def call_mistral(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {LLM_3_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": os.getenv("LLM_3_MODEL", "accounts/fireworks/models/mixtral-8x7b-instruct"),
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post(LLM_3_ENDPOINT, json=payload, headers=headers, timeout=30)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()

def generate_text(prompt: str) -> str:
    for provider, func in [("OpenAI", call_openai), ("Anthropic", call_anthropic), ("Mistral", call_mistral)]:
        try:
            return func(prompt)
        except Exception as e:
            print(f"[LLM Service] Falha em {provider}: {e}")
    raise RuntimeError("Todos os provedores LLM falharam.")
