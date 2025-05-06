# 📄 Documentação do Script: Gerador de Embeddings com Ollama API

## ✨ Descrição

Este script em Python permite gerar _embeddings_ (representações vetoriais) a partir de um texto fornecido pelo usuário, utilizando a API local da **Ollama**. A geração de embeddings é útil em aplicações de **NLP** (Processamento de Linguagem Natural), como busca semântica, clustering e análise de similaridade.

---

## 🚀 Requisitos

- Python 3.x
- Biblioteca `requests` instalada  
  _(pode ser instalada com `pip install requests`)_
- Servidor **Ollama** rodando localmente na porta `11434` com o endpoint `/api/embeddings` disponível.
- Modelo de embedding chamado `"nomic-embed-text"` disponível no Ollama.
  _(pode ser instalado usando `ollama pull nomic-embed-text`)_

---

## 🧩 Descrição das Variáveis e Funções

| Variável/Função      | Descrição                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `OLLAMA_URL`         | String que armazena a URL base da API Ollama local para geração de embeddings (`http://localhost:11434/api/embeddings`). |
| `texto`              | Entrada do usuário que solicita a digitação de um texto para ser convertido em embedding.                                |
| `requests.post(...)` | Faz uma requisição POST enviando o texto para a API Ollama em formato JSON.                                              |
| `response.json()`    | Converte a resposta da API de JSON para um dicionário Python e imprime o resultado.                                      |

---

## 🔄 Fluxo do Programa

1. O script solicita ao usuário que digite o texto desejado.
2. Uma requisição POST é enviada para o endpoint `/api/embeddings`, com:
   - **model**: `"nomic-embed-text"`
   - **prompt**: texto digitado pelo usuário.
3. O script imprime a resposta JSON, que contém o embedding gerado (um vetor numérico) e possíveis metadados.

---

## 📌 Exemplo de Uso

```bash
$ python gerador_embeddings.py
Digite o texto para gerar o embedding: Machine learning é incrível!
{'embedding': [...], 'model': 'nomic-embed-text', 'created_at': '...', ...}
```
