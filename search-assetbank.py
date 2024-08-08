import requests
import time

# API Configuration
API_BASE_URL = "https://your_assetbank_url"
ACCESS_TOKEN = "your_access_token_here"  # Replace with your access token
REFRESH_TOKEN = "your_refresh_token_here"  # Replace with your refresh token
CLIENT_ID = "your_client_id_here"  # Replace with your client ID
CLIENT_SECRET = "your_client_secret_here"  # Replace with your client secret
TOKEN_URL = f"{API_BASE_URL}/oauth/token"

# Function to refresh the token
def refresh_access_token():
    global ACCESS_TOKEN, REFRESH_TOKEN
    payload = {
        'grant_type': 'refresh_token',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN
    }
    
    response = requests.post(TOKEN_URL, data=payload)
    
    if response.status_code == 200:
        token_data = response.json()
        ACCESS_TOKEN = token_data['access_token']
        REFRESH_TOKEN = token_data['refresh_token']
        print("Token refreshed successfully.")
    else:
        print(f"Failed to refresh token: {response.status_code}")
        print(response.text)

# Function to make the API request with token management
def make_api_request():
    global ACCESS_TOKEN
    url = f"{API_BASE_URL}/rest/asset-search"
    params = {
        "keywords": "villas",
        "page": 0,
        "pageSize": 10,
        "sortAttributeId": 1,
        "sortDescending": "false"
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json"
    }
    print(headers)
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 401:  # Token expired
        print("Access token expired. Refreshing token...")
        refresh_access_token()
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
        response = requests.get(url, headers=headers, params=params)
    
    print(response)
    print(response.text)

# Example usage
make_api_request()
