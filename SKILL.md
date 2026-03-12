---
name: olaxbt-nexus-data
version: 1.0.0
description: "Official OlaXBT Nexus Data API skill for OpenClaw agents. Provides real-time crypto market data, news, KOL tracking, technical indicators, and comprehensive market analysis through wallet-authenticated API endpoints."
author: "OlaXBT Team"
license: "MIT"
repository: "https://github.com/olaxbt/olaxbt-skills-hub"
metadata:
  openclaw:
    emoji: "🔮"
    requires:
      bins: []
      env:
        - "ETH_WALLET_ADDRESS"
        - "ETH_PRIVATE_KEY"
      python: ">=3.8"
    install:
      - id: "pip"
        kind: "pip"
        package: "olaxbt-nexus-data"
        label: "Install via pip"
    categories:
      - "crypto"
      - "data"
      - "trading"
    permissions:
      - "network"
      - "environment_variables"
    security_level: "high"
    rate_limits:
      auth: "10 requests/hour"
      data: "1000 requests/hour"
---

# OlaXBT Nexus Data Skill

## Overview
Official OlaXBT Nexus Data API integration for OpenClaw agents. This skill provides access to real-time cryptocurrency market data, news, KOL tracking, technical indicators, and comprehensive market analysis through a secure wallet-authenticated API.

## Features
- **14 Comprehensive API Endpoints**: Full coverage of OlaXBT Nexus data services
- **Secure Wallet Authentication**: Ethereum wallet-based JWT authentication
- **Real-time Market Data**: Live crypto market insights and analysis
- **KOL & Sentiment Tracking**: Monitor key opinion leaders and market sentiment
- **Technical Indicators**: Advanced trading signals and analysis
- **Smart Money Tracking**: Follow institutional and smart money flows
- **News Aggregation**: Curated crypto news from multiple sources

## API Endpoints

### 1. AIO Assistant (`/assistant`)
Market analysis and trading signals for automated trading strategies.

### 2. Ask Nexus (`/ask-nexus`)
AI-powered cryptocurrency chat and analysis (credits may apply).

### 3. News API (`/news`)
Crypto news aggregation, search, summarization, and analytics.

### 4. KOL API (`/kol`)
Key Opinion Leader tracking, tweet analysis, and symbol heatmaps.

### 5. Technical Indicators (`/technical-indicators`)
Trading signals, historical analysis, and technical indicators.

### 6. Smart Money (`/smart-money`)
Institutional money tracking, token analysis, and divergence detection.

### 7. Liquidations (`/liquidations`)
Liquidation data, open interest history, and funding rates.

### 8. Market Divergence (`/divergences`)
Market divergence detection across OI, funding, and smart money.

### 9. Sentiment (`/sentiment`)
Market sentiment analysis and trend tracking.

### 10. ETF (`/etf`)
ETF inflow/outflow tracking and metrics.

### 11. Market Overview (`/market`)
Comprehensive crypto and stock market overview.

### 12. Open Interest (`/oi`)
Open interest rate-of-change, symbol OI, and rankings.

### 13. Coin Data (`/coin`)
Per-coin data including price, OI, netflow, and price changes.

### 14. Credits & Top-up
Credit balance management and purchase verification.

## Authentication

### Base URLs
- **Auth Domain**: `https://api.olaxbt.xyz/api`
- **Data Domain**: `https://api-data.olaxbt.xyz/api/v1`

### Authentication Flow
1. **Get Auth Message**: Request a one-time message to sign
2. **Sign Message**: Sign with Ethereum wallet using `personal_sign`
3. **Get JWT**: Exchange signature for JWT token
4. **Access API**: Use JWT for all data API requests

### Security Notes
- Never expose private keys in code or logs
- Store JWT tokens securely with encryption
- Use environment variables for sensitive data
- Implement rate limiting to prevent API abuse

## Installation

### For OpenClaw Users
```bash
# Install from ClawHub
openclaw skill install olaxbt-nexus-data
```

### For Python Developers
```bash
pip install olaxbt-nexus-data
```

### Environment Variables
```bash
export ETH_WALLET_ADDRESS="0xYourWalletAddress"
export ETH_PRIVATE_KEY="0xYourPrivateKey"
```

## Quick Start

```python
from olaxbt_nexus_data import NexusClient

# Initialize client with environment variables
client = NexusClient()

# Authenticate (automatically handles JWT)
client.authenticate()

# Get latest news
news = client.news.get_latest(limit=10)

# Get market overview
market = client.market.get_overview()

# Get KOL heatmap
kol_data = client.kol.get_heatmap(symbol="BTC")
```

## Examples

See the `examples/` directory for complete usage examples:
- `basic_usage.py` - Basic authentication and API calls
- `news_monitor.py` - Real-time news monitoring
- `market_analysis.py` - Comprehensive market analysis
- `wallet_auth.py` - Advanced wallet authentication

## Security Best Practices

1. **Private Key Management**
   - Use environment variables only
   - Never commit private keys to version control
   - Rotate keys regularly

2. **JWT Token Security**
   - Tokens expire after 1 hour
   - Automatic refresh implemented
   - Encrypted storage in memory

3. **API Usage**
   - Respect rate limits (1000 requests/hour)
   - Implement exponential backoff for retries
   - Cache responses when appropriate

## Support

- **Documentation**: [https://olaxbt.xyz/skill.md](https://olaxbt.xyz/skill.md)
- **GitHub**: [https://github.com/olaxbt/olaxbt-skills-hub](https://github.com/olaxbt/olaxbt-skills-hub)
- **Issues**: Report via GitHub issues

## License

MIT License - See LICENSE file for details.

---

*This skill is officially maintained by the OlaXBT Team.*