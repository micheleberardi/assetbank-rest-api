from flask import Flask, redirect, url_for, session, request, jsonify
from authlib.integrations.flask_client import OAuth
import secrets  # For generating a secure state
import traceback  # Import traceback module

# Static configuration values
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
AUTHORIZATION_BASE_URL = 'https://your_assetbank_url/oauth/authorize'
TOKEN_URL = 'https://your_assetbank_url/oauth/token'
REDIRECT_URI = 'https://your_redirect_uri/callback'
API_BASE_URL = 'https://your_assetbank_url/'
SECRET_KEY = 'your_secret_key_here'

app = Flask(__name__)
app.secret_key = SECRET_KEY

# OAuth Configuration with Authlib
oauth = OAuth(app)
assetbank = oauth.register(
    name='assetbank',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token_url=TOKEN_URL,
    authorize_url=AUTHORIZATION_BASE_URL,
    api_base_url=API_BASE_URL,
    client_kwargs={
        'scope': 'read',  # Specify the requested permissions
    }
)

@app.route('/')
def home():
    return '<a href="/login">Login with Asset Bank</a>'

@app.route('/login')
def login():
    # Generate a secure state and save it in the session
    state = secrets.token_urlsafe(16)
    session['oauth_state'] = state
    
    print(f"State generated and saved: {state}")
    
    # Generate an authorization URL with state
    return assetbank.authorize_redirect(REDIRECT_URI, state=state)

@app.route('/callback')
def callback():
    try:
        # Retrieve the state from the session and compare it with the received one
        expected_state = session.pop('oauth_state', None)
        actual_state = request.args.get('state')
        
        print(f"Expected state: {expected_state}, Received state: {actual_state}")
        
        if expected_state != actual_state:
            return 'Error: State does not match', 400
        
        # Obtain the access token
        token = assetbank.authorize_access_token()
        
        if not token:
            print("Error: Token not received.")
            return 'Error obtaining the token', 400
        
        print("Token obtained:", token)
        return jsonify(token)
    
    except Exception as e:
        print(f"Error during callback process: {e}")
        traceback.print_exc()  # Print the full traceback
        return 'Error in callback process', 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=22017)
