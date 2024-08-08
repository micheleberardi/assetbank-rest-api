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

# Function to search for images with token management
def search_images(params):
    global ACCESS_TOKEN
    url = f"{API_BASE_URL}/rest/asset-search"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 401:  # Token expired
        print("Access token expired. Refreshing token...")
        refresh_access_token()
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
        response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print("Search results:", data)
        return data  # Return data directly
    else:
        print(f"Error in image search: {response.status_code}")
        return None

# Function to download the image with token management
def download_image(asset_id, file_path):
    global ACCESS_TOKEN
    url = f"{API_BASE_URL}/rest/assets/{asset_id}/content"
    print(url)
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    response = requests.get(url, headers=headers, stream=True)
    
    if response.status_code == 401:  # Token expired
        print("Access token expired. Refreshing token...")
        refresh_access_token()
        headers["Authorization"] = f"Bearer {ACCESS_TOKEN}"
        response = requests.get(url, headers=headers, stream=True)
    
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image successfully downloaded to {file_path}")
    else:
        print(f"Error in downloading image: {response.status_code}")

# Example usage
params = {
    "assetIds": "1",
    "page": 0,
    "pageSize": 10,
    "sortAttributeId": 1,
    "sortDescending": "false"
}

images = search_images(params)
print("Images found:", images)

if images and len(images) > 0:
    # Suppose we want to download the first image found
    first_image = images[0]
    asset_id = first_image['id']
    file_path = f"{first_image['originalFilename']}"  # Save the image with the original filename
    
    download_image(asset_id, file_path)
else:
    print("No images found.")
