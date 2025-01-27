# Social Authentication with Python
This repository demonstrates social authentication with Python via API calls to the providers' (currently Google) OAuth endpoints.

## Google API Endpoints Used 🛠
The application makes use of three endpoints from the Google API.
-  `https://accounts.google.com/o/oauth2/v2/auth` - To get the consent page and redirect to the callback endpoint provided in the application.

- `https://oauth2.googleapis.com/token` - To exchange an authorization code for an access token.

- `https://www.googleapis.com/oauth2/v2/userinfo` - To get the user information with the acccess token.

## Installation 👷‍♂️
1. Clone the repository
    ```
    git clone https://github.com/tegarorobi/social-auth-with-python.git
    ```

2. Install the requirements
    ```
    python -m pip install -r requirements.txt
    ```

3. Run the development server (default is port 8000)
    ```
    python manage.py runserver
    ```

4. Click on the `Login with Google` link in the home page. You would be redirected to the OAuth consent page. After accepting the connection, the user credentials (id, name, email, profile picture) would be returned in the browser.

### Note 📝
- This Google article explains the entire processs in detailed, easy-to-follow steps [https://developers.google.com/identity/protocols/oauth2/web-server#httprest_6](https://developers.google.com/identity/protocols/oauth2/web-server#httprest_6)
- Thec callback URL in the _redirect_uri_ parameter sent to the OAuth API should match the one registered when creating the Google web client credentials in the Google cloud platform dashboard.