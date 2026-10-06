import os
from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

# 1. Monitoring & API Setup
os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
os.environ.setdefault("LANGCHAIN_PROJECT", "Nebius-Binance-Sentinel")

NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY", "dummy-key-for-init")
NEBIUS_BASE_URL = os.getenv("NEBIUS_BASE_URL", "https://api.tokenfactory.nebius.ai/v1")

# 2. Schema
class MarketAnalysis(BaseModel):
    symbol: str = Field(description="Crypto asset ticker e.g. BTC, ETH, SOL")
    sentiment_score: float = Field(description="Sentiment from -1.0 to +1.0")
    key_drivers: list[str] = Field(description="Key market drivers or news factors")
    risk_level: str = Field(description="Risk level: LOW, MEDIUM, HIGH, CRITICAL")
    action_recommendation: str = Field(description="STRONG_BUY, BUY, HOLD, SELL, or STRONG_SELL")
    reasoning: str = Field(description="Detailed reasoning for the decision")

# 3. Agent Engine
class AgenticSentinel:
    def __init__(self, model_name: str = "meta-llama/Meta-Llama-3.1-70B-Instruct"):
        self.llm = ChatOpenAI(
            model=model_name,
            openai_api_key=NEBIUS_API_KEY,
            base_url=NEBIUS_BASE_URL,
            temperature=0.2,
        )
        self.parser = JsonOutputParser(pydantic_object=MarketAnalysis)

    def analyze_asset(self, symbol: str, market_context: str, news_feed: str) -> Dict[str, Any]:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are Sentinel-AI, an autonomous crypto quant & risk agent. Analyze market objectively.\n{format_instructions}"),
            ("user", "Analyze asset: {symbol}\n\nMarket Context:\n{context}\n\nNews Feed:\n{news}"),
        ])
        chain = prompt | self.llm | self.parser
        try:
            return chain.invoke({
                "symbol": symbol,
                "context": market_context,
                "news": news_feed,
                "format_instructions": self.parser.get_format_instructions(),
            })
        except Exception as e:
            return {"error": str(e), "symbol": symbol, "status": "fallback"}

if __name__ == "__main__":
    print("🚀 Initializing Nebius-Binance Agentic Sentinel...")
    agent = AgenticSentinel()
    print("✅ Agent pipeline compiled successfully.")
