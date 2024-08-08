# OAuth Flask Application with Asset Bank

This is a simple Flask application demonstrating how to implement OAuth2 authentication with Asset Bank.

## Prerequisites

- Python 3.6+
- Flask
- Authlib
- Secrets module (comes with Python 3.6+)
- Traceback module (comes with Python 3.6+)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/micheleberardi/assetbank-rest-api.git
    cd assetbank-rest-api
    ```

2. Install the required packages:
    ```bash
    pip install Flask Authlib
    ```

## Configuration

Replace the placeholder values in the script with your actual configuration values.

```python
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
AUTHORIZATION_BASE_URL = 'https://your_assetbank_url/oauth/authorize'
TOKEN_URL = 'https://your_assetbank_url/oauth/token'
REDIRECT_URI = 'https://your_redirect_uri/callback'
API_BASE_URL = 'https://your_assetbank_url/'
SECRET_KEY = 'your_secret_key_here'

