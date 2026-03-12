# OlaXBT Nexus Data API Skill

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)
![License](https://img.shields.io/badge/license-MIT-yellow)
![OpenClaw](https://img.shields.io/badge/OpenClaw-2026.3.0%2B-orange)

Official OlaXBT Nexus Data API integration for OpenClaw agents. This skill provides secure, wallet-authenticated access to real-time cryptocurrency market data, news, KOL tracking, and comprehensive market analysis.

## Features

- **🔐 Secure Authentication**: Ethereum wallet-based JWT authentication
- **📊 14 API Endpoints**: Full coverage of OlaXBT Nexus data services
- **⚡ Real-time Data**: Live market insights and analysis
- **🛡️ Enterprise Security**: Military-grade security implementation
- **🔄 Automatic Token Refresh**: Seamless JWT management
- **📈 Advanced Analytics**: Technical indicators and smart money tracking

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

### Environment Setup
```bash
# Set your Ethereum wallet credentials
export ETH_WALLET_ADDRESS="0xYourWalletAddress"
export ETH_PRIVATE_KEY="0xYourPrivateKey"
```

## Quick Start

```python
from olaxbt_nexus_data import NexusClient

# Initialize client (uses environment variables)
client = NexusClient()

# Authenticate automatically
client.authenticate()

# Get latest crypto news
news = client.news.get_latest(limit=10)
for item in news:
    print(f"📰 {item['title']}")

# Get market overview
market = client.market.get_overview()
print(f"📈 Total Market Cap: ${market['total_market_cap']:,.0f}")

# Get KOL heatmap for Bitcoin
kol_data = client.kol.get_heatmap(symbol="BTC")
print(f"👥 KOL Activity: {kol_data['total_mentions']} mentions")
```

## API Endpoints

| Endpoint | Description | Credits Required |
|----------|-------------|------------------|
| **AIO Assistant** | Market analysis & trading signals | Yes |
| **Ask Nexus** | AI crypto chat & analysis | Yes |
| **News API** | Crypto news aggregation | No |
| **KOL API** | Key Opinion Leader tracking | No |
| **Technical Indicators** | Trading signals & analysis | No |
| **Smart Money** | Institutional money tracking | No |
| **Liquidations** | Liquidation data & OI history | No |
| **Market Divergence** | Market divergence detection | No |
| **Sentiment** | Market sentiment analysis | No |
| **ETF** | ETF inflow/outflow tracking | No |
| **Market Overview** | Comprehensive market overview | No |
| **Open Interest** | OI rate-of-change & rankings | No |
| **Coin Data** | Per-coin data & metrics | No |
| **Credits Management** | Balance & purchase verification | N/A |

## Authentication

### Base URLs
- **Auth Domain**: `https://api.olaxbt.xyz/api`
- **Data Domain**: `https://api-data.olaxbt.xyz/api/v1`

### Authentication Flow
```python
# The client handles authentication automatically
client = NexusClient(
    wallet_address="0x...",  # Optional: override env var
    private_key="0x..."      # Optional: override env var
)

# Manual authentication if needed
jwt_token = client.auth.get_jwt()
print(f"JWT Token: {jwt_token[:50]}...")
```

## Security Features

### Private Key Protection
- Never stored in plain text
- Environment variables only
- Encrypted in memory
- Automatic cleanup

### JWT Management
- 1-hour expiration
- Automatic refresh
- Encrypted storage
- Secure transmission

### API Security
- Rate limiting (1000 requests/hour)
- Input validation
- Error sanitization
- HTTPS enforcement

## Examples

Check the `examples/` directory for complete implementations:

### `examples/basic_usage.py`
Basic authentication and API calls demonstration.

### `examples/news_monitor.py`
Real-time news monitoring with filtering and alerts.

### `examples/market_analysis.py`
Comprehensive market analysis with multiple data sources.

### `examples/wallet_auth.py`
Advanced wallet authentication and JWT management.

## Configuration

### Environment Variables
```bash
# Required
ETH_WALLET_ADDRESS="0xYourWalletAddress"
ETH_PRIVATE_KEY="0xYourPrivateKey"

# Optional
NEXUS_AUTH_URL="https://api.olaxbt.xyz/api"
NEXUS_DATA_URL="https://api-data.olaxbt.xyz/api/v1"
REQUEST_TIMEOUT="30"
MAX_RETRIES="3"
```

### Client Configuration
```python
from olaxbt_nexus_data import NexusClient

client = NexusClient(
    # Override environment variables
    wallet_address="0x...",
    private_key="0x...",
    
    # Custom configuration
    auth_url="https://api.olaxbt.xyz/api",
    data_url="https://api-data.olaxbt.xyz/api/v1",
    timeout=30,
    max_retries=3,
    
    # Security settings
    encrypt_jwt=True,
    rate_limit=1000,  # requests per hour
)
```

## Error Handling

```python
from olaxbt_nexus_data import NexusClient, NexusError

client = NexusClient()

try:
    data = client.news.get_latest(limit=10)
except NexusError as e:
    print(f"API Error: {e.message}")
    print(f"Status Code: {e.status_code}")
except AuthenticationError as e:
    print(f"Authentication failed: {e.message}")
    # Re-authenticate or check credentials
except RateLimitError as e:
    print(f"Rate limit exceeded: {e.message}")
    print(f"Reset in: {e.reset_in} seconds")
```

## Testing

```bash
# Install development dependencies
pip install olaxbt-nexus-data[dev]

# Run tests
pytest tests/

# Run with coverage
pytest --cov=olaxbt_nexus_data tests/

# Type checking
mypy src/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Support

- **Documentation**: [https://olaxbt.xyz/skill.md](https://olaxbt.xyz/skill.md)
- **GitHub Issues**: [https://github.com/olaxbt/olaxbt-nexus-data/issues](https://github.com/olaxbt/olaxbt-nexus-data/issues)
- **Email**: hello@olaxbt.xyz

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Official OlaXBT Skill** • **Enterprise Grade** • **Production Ready**