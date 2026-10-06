# 🛡️ Binance Agentic Sentinel

**Autonomous Crypto Quant & Risk Agent** powered by Nebius AI, LangChain & LangSmith.

An agentic AI system that autonomously monitors crypto markets, analyzes news sentiment, and delivers structured risk assessments (LOW → CRITICAL) with actionable recommendations (STRONG_BUY → STRONG_SELL) — fully in JSON.

## 🚀 Problem
Crypto traders drown in scattered data: prices, news, and sentiment live in different places. Humans react slowly and emotionally.

## 💡 Solution
Sentinel-AI is a autonomous LLM agent that:
- 🔍 Ingests market context & live news feeds (via Tavily)
- 🧠 Reasons over them using **Llama-3.1-70B** on **Nebius Token Factory**
- 📊 Outputs **structured, machine-readable analysis** (Pydantic-validated JSON)
- 📡 Is fully **observable & debuggable** via **LangSmith** tracing

## ⚙️ Tech Stack
| Layer | Tool |
|---|---|
| LLM Engine | Nebius Token Factory (Llama-3.1-70B-Instruct) |
| Agent Framework | LangChain + LangGraph |
| Observability | LangSmith |
| Market Data | CCXT (100+ exchanges) |
| News Retrieval | Tavily API |

## 🏃 Quick Start
```bash
pip install -r requirements.txt
export NEBIUS_API_KEY="your-key"
python agent.py
# binance-agentic-sentinel
Autonomous AI Trading &amp; Sentiment Sentinel Agentpowered by Nebius, LangChain, and LangSmith
