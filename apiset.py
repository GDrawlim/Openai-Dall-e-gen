import os 

os.environ['OPENAI_API_KEY'] = 'your_key'
import openai

# Retrieve the API key from the environment variable
api_key = os.environ.get('OPENAI_API_KEY')

# Set the API key for the openai package
openai.api_key = api_key

# Generate text using the GPT API
prompt = "Hello, my name is"
response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=5)
print(response.choices[0].text)
