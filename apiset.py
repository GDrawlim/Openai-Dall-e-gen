import os 

os.environ['OPENAI_API_KEY'] = 'api-key'
import openai

# Retrieve the API key from the environment variable
api_key = os.environ.get('OPENAI_API_KEY')

# Set the API key for the openai package
openai.api_key = api_key

# Generate text using the GPT API
prompt = "Hello, my name is"
response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=5)
print(response.choices[0].text)

import requests
import configparser

# Read the access token from the configuration file
config = configparser.ConfigParser()
config.read('config.ini')
access_token = config.get('github', 'access_token')

# Set the authorization header with the access token
headers = {'Authorization': f'token {access_token}'}

# Make an API request to retrieve repository information
url = 'https://api.github.com/repos/octocat/hello-world'
response = requests.get(url, headers=headers)

# Handle the API response
if response.status_code == 200:
    data = response.json()
    print(data['full_name'])
else:
    print('API request failed')

import stripe
import os
from flask import Flask, request, jsonify

# Retrieve the API key from the environment variable
api_key = os.environ.get('STRIPE_API_KEY')

# Set up the Stripe API key
stripe.api_key = api_key

# Set up the Flask app
app = Flask(__name__)

# Define a route for the login page
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # Verify the user's credentials
    # ...
    # Return an access token
    access_token = 'your_access_token'
    return jsonify({'access_token': access_token})

# Define a route for the payment page
@app.route('/payment', methods=['POST'])
def payment():
    # Retrieve the access token from the request headers
    access_token = request.headers.get('Authorization').split(' ')[1]

    # Verify the user's access token
    # ...

    # Create a payment using the Stripe API
    payment_intent = stripe.PaymentIntent.create(
        amount=1000,
        currency='usd',
        payment_method_types=['card'],
    )

    # Get the payment intent ID
    payment_intent_id = payment_intent['id']

    # Return the payment intent ID to the client
    return jsonify({'payment_intent_id': payment_intent_id})

if __name__ == '__main__':
    app.run()