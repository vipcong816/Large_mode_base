# -*- coding: utf-8 -*-

from zhipuai import ZhipuAI
import configparser

# Function to read API key from config file
def read_glm4_key(file_path,Credentialsid):
    config = configparser.ConfigParser()
    config.read(file_path)
    api_key = config.get('Credentials', 'api_key')
    return api_key.strip()

# Function to read query from file
def read_query_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()
    return query.strip()

# Function to interact with ZhipuAI API
def stream_glm4(prompt_file_path, config_file_path):
    try:
        # Read API key from config file
        api_key = read_glm4_key(config_file_path)

        # Initialize ZhipuAI client with your API key
        client = ZhipuAI(api_key=api_key)

        # Read query from prompt file
        query = read_query_from_file(prompt_file_path)

        # Call the ZhipuAI API to get response
        response = client.chat.completions.create(
            model="glm-4",  # Specify the model name you want to use
            messages=[
                {"role": "user", "content": query},
            ],
            stream=True,
        )

        # Iterate over response chunks
        for chunk in response:
            print(chunk.choices[0].delta.content)  # Output the response content

    except Exception as e:
        print(e)

# Paths to the prompt file and config file
prompt_file_path = 'prompt.md'
config_file_path = 'config.ini'

# Call the function to interact with ZhipuAI
stream_glm4(prompt_file_path, config_file_path)




