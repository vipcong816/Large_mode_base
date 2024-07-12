# -*- coding: utf-8 -*-


import configparser
from zhipuai import ZhipuAI  # Assuming ZhipuAI is imported correctly from the correct package

class ZhipuAIClient:
    def __init__(self, config_file_path):
        self.api_key = self.read_glm4_key(config_file_path)
        self.client = ZhipuAI(api_key=self.api_key)

    def read_glm4_key(self, file_path):
        config = configparser.ConfigParser()
        config.read(file_path)
        api_key = config.get('Credentials', 'api_key')
        return api_key.strip()

    def read_query_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            query = file.read()
        return query.strip()

    def stream_glm4(self, prompt_file_path):
        try:
            # Read query from prompt file
            query = self.read_query_from_file(prompt_file_path)

            # Call the ZhipuAI API to get response
            response = self.client.chat.completions.create(
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
            
    def generate_images(self, prompt):
        try:
            # Call the ZhipuAI API to generate images
            response = self.client.images.generations(
                model="cogview-3",  # Specify the model name you want to use
                prompt=prompt,  # Provide the prompt for generating images
            )

            return response  # Return the entire response object

        except Exception as e:
            print(e)
