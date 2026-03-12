"""
OlaXBT Nexus Data API Client

Official Python client for the OlaXBT Nexus Data API.
Provides secure, wallet-authenticated access to cryptocurrency market data,
news, KOL tracking, technical indicators, and comprehensive market analysis.
"""

__version__ = "1.0.0"
__author__ = "OlaXBT Team"
__email__ = "contact@olaxbt.xyz"
__license__ = "MIT"

import os
import logging
from typing import Optional, Dict, Any

from .core.auth import NexusAuth
from .core.client import NexusAPIClient
from .core.security import SecurityConfig
from .api.news import NewsClient
from .api.kol import KOLClient
from .api.market import MarketClient
from .api.technical import TechnicalClient
from .api.smart_money import SmartMoneyClient
from .api.liquidations import LiquidationsClient
from .api.sentiment import SentimentClient
from .api.etf import ETFClient
from .api.oi import OIClient
from .api.coin import CoinClient
from .api.assistant import AssistantClient
from .api.ask_nexus import AskNexusClient
from .api.divergences import DivergencesClient
from .api.credits import CreditsClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class NexusClient:
    """Main client for OlaXBT Nexus Data API."""
    
    def __init__(
        self,
        wallet_address: Optional[str] = None,
        private_key: Optional[str] = None,
        auth_url: Optional[str] = None,
        data_url: Optional[str] = None,
        timeout: int = 30,
        max_retries: int = 3,
        encrypt_jwt: bool = True,
        rate_limit: int = 1000,
    ):
        """
        Initialize the Nexus client.
        
        Args:
            wallet_address: Ethereum wallet address (optional, uses env var)
            private_key: Ethereum private key (optional, uses env var)
            auth_url: Authentication API URL (optional)
            data_url: Data API URL (optional)
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts
            encrypt_jwt: Whether to encrypt JWT tokens in memory
            rate_limit: Maximum requests per hour
            
        Raises:
            ValueError: If required credentials are missing
        """
        # Get credentials from environment or parameters
        self.wallet_address = wallet_address or os.getenv("ETH_WALLET_ADDRESS")
        self.private_key = private_key or os.getenv("ETH_PRIVATE_KEY")
        
        if not self.wallet_address:
            raise ValueError(
                "Wallet address is required. "
                "Set ETH_WALLET_ADDRESS environment variable or pass wallet_address parameter."
            )
        
        if not self.private_key:
            raise ValueError(
                "Private key is required. "
                "Set ETH_PRIVATE_KEY environment variable or pass private_key parameter."
            )
        
        # Configure URLs
        self.auth_url = auth_url or os.getenv("NEXUS_AUTH_URL", "https://api.olaxbt.xyz/api")
        self.data_url = data_url or os.getenv("NEXUS_DATA_URL", "https://api-data.olaxbt.xyz/api/v1")
        
        # Security configuration
        self.security_config = SecurityConfig(
            encrypt_jwt=encrypt_jwt,
            rate_limit=rate_limit,
            timeout=timeout,
            max_retries=max_retries,
        )
        
        # Initialize authentication
        self.auth = NexusAuth(
            wallet_address=self.wallet_address,
            private_key=self.private_key,
            auth_url=self.auth_url,
            security_config=self.security_config,
        )
        
        # Initialize API client
        self.api_client = NexusAPIClient(
            auth_client=self.auth,
            data_url=self.data_url,
            security_config=self.security_config,
        )
        
        # Initialize API clients
        self.news = NewsClient(self.api_client)
        self.kol = KOLClient(self.api_client)
        self.market = MarketClient(self.api_client)
        self.technical = TechnicalClient(self.api_client)
        self.smart_money = SmartMoneyClient(self.api_client)
        self.liquidations = LiquidationsClient(self.api_client)
        self.sentiment = SentimentClient(self.api_client)
        self.etf = ETFClient(self.api_client)
        self.oi = OIClient(self.api_client)
        self.coin = CoinClient(self.api_client)
        self.assistant = AssistantClient(self.api_client)
        self.ask_nexus = AskNexusClient(self.api_client)
        self.divergences = DivergencesClient(self.api_client)
        self.credits = CreditsClient(self.api_client)
        
        logger.info(f"Nexus client initialized for wallet: {self.wallet_address[:10]}...")
    
    def authenticate(self) -> str:
        """
        Authenticate with the Nexus API and get JWT token.
        
        Returns:
            JWT token string
            
        Raises:
            AuthenticationError: If authentication fails
        """
        return self.auth.authenticate()
    
    def get_credits_balance(self) -> Dict[str, Any]:
        """
        Get current credits balance.
        
        Returns:
            Dictionary with credits information
            
        Raises:
            APIError: If API request fails
        """
        return self.api_client.get_credits_balance()
    
    def health_check(self) -> bool:
        """
        Check if the API is healthy and accessible.
        
        Returns:
            True if API is healthy, False otherwise
        """
        try:
            response = self.api_client._request("GET", "health")
            return response.get("status") == "healthy"
        except Exception:
            return False
    
    def __repr__(self) -> str:
        """String representation of the client."""
        return f"NexusClient(wallet={self.wallet_address[:10]}..., url={self.data_url})"


# Export main classes
__all__ = [
    "NexusClient",
    "NexusAuth",
    "NexusAPIClient",
    "NewsClient",
    "KOLClient",
    "MarketClient",
    "TechnicalClient",
    "SmartMoneyClient",
    "LiquidationsClient",
    "SentimentClient",
    "ETFClient",
    "OIClient",
    "CoinClient",
    "AssistantClient",
    "AskNexusClient",
    "DivergencesClient",
    "CreditsClient",
]

# Export exceptions
from .core.exceptions import (
    NexusError,
    AuthenticationError,
    APIError,
    RateLimitError,
    ValidationError,
)

__all__.extend([
    "NexusError",
    "AuthenticationError",
    "APIError",
    "RateLimitError",
    "ValidationError",
])