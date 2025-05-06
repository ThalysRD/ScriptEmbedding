import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"

texto = input("Digite o texto para gerar o embedding: ")
response = requests.post(OLLAMA_URL, json={"model": "nomic-embed-text", "prompt": texto})
print(response.json())
