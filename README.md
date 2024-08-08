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

Running the Application
Run the Flask application:

bash
Copy code
python app.py
Navigate to http://127.0.0.1:22017 in your browser.

Click on "Login with Asset Bank" to start the OAuth2 flow.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Flask
Authlib
markdown
Copy code

### Summary:
1. **Script**: The Python script includes placeholder values for client ID, client secret, and URLs.
2. **README.md**: The README file provides setup instructions, including prerequisites, installation steps, configuration details, and how to run the application.
3. **License**: Mention that the project is licensed under the MIT License (you should add a LICENSE file if you include this in the README).

This setup will help others understand how to configure and run the application with
