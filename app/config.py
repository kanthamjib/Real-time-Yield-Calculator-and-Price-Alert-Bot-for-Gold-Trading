"""
config.py
---------

This module defines the configuration settings for the Real-time Yield Calculator
and Price Alert Bot for Gold Trading project. It includes API keys and other
environment-specific variables required to connect to Alpha Vantage and LINE Messaging APIs.

Author: MiniJibli
Date: 2024-11-02
Project: Real-time Yield Calculator and Price Alert Bot for Gold Trading

Settings:
- ALPHA_VANTAGE_API_KEY: API key for accessing Alpha Vantage's real-time gold price data.
- LINE_ACCESS_TOKEN: Token for authenticating with LINE Messaging API.
- PRICE_CHECK_INTERVAL: Frequency (in seconds) for fetching updated gold prices.

Usage:
    Import this module to access configuration variables:
        from app.config import ALPHA_VANTAGE_API_KEY
"""

# API keys for Alpha Vantage and LINE Messaging
ALPHA_VANTAGE_API_KEY = "your_alpha_vantage_api_key"
LINE_ACCESS_TOKEN = "your_line_access_token"

# Interval for checking gold prices in every 12 seconds
PRICE_CHECK_INTERVAL = 12
