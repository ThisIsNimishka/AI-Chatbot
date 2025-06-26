import json
import openai

# Set your OpenAI API key
openai.api_key = 'your-api-key'

# Define your prompt (user query)
prompt = "Hello, how are you?"

# Make an API request to get the model's response
response = openai.Completion.create(
    engine="text-davinci-002",  # Choose the GPT model
    prompt=prompt,
    max_tokens=50  # Set the maximum number of tokens for the response
)

# Extract the model's response from the API response
chatGPT_response = response.choices[0].text.strip()

# Create a dictionary to store the data
data = {
    "prompt": prompt,
    "response": chatGPT_response
}

# Save the data to a JSON file
with open('chat_data.json', 'a') as file:
    json.dump(data, file)
    file.write('\n')  # Add a new line for each entry
