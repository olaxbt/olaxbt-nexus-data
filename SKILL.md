---
name: olaxbt-nexus-data
description: "Access OlaXBT Nexus cryptocurrency data APIs including market data, news, KOL tracking, technical indicators, and wallet-authenticated analysis for trading insights."
metadata: {"openclaw": {"requires": {"env": ["ETH_WALLET_ADDRESS"]}}}
---

# OlaXBT Nexus Data Skill

This skill provides access to OlaXBT Nexus cryptocurrency data APIs.

## When to use this skill
- When you need real-time cryptocurrency market data
- When you want to analyze crypto news and sentiment
- When tracking key opinion leaders (KOLs) in crypto
- When analyzing technical indicators for trading
- When monitoring smart money flows

## Features
- 14 comprehensive API endpoints
- Secure wallet authentication
- Real-time market data
- KOL and sentiment tracking
- Technical indicators analysis

## Installation
```bash
pip install olaxbt-nexus-data
```

## Quick Start
```python
from olaxbt_nexus_data import NexusAuth, NexusAPIClient
auth = NexusAuth(wallet_address="0x...")
api = NexusAPIClient(auth_client=auth)
news = api.get_news(limit=10)
```

## Security
- Use environment variables for private keys
- All API calls use HTTPS
- Rate limiting implemented

## Repository
https://github.com/olaxbt/olaxbt-nexus-data
