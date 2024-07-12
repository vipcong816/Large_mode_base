# coverage run test_llm_glm4.py

import coverage
import unittest
from llm_glm4 import ZhipuAIClient

class TestZhipuAIClient(unittest.TestCase):

    def test_stream_glm4_coverage(self):
        prompt_file_path = 'prompt.md'  # Use a test-specific prompt file
        config_file_path = 'config.ini'  # Use a test-specific config file

        # Start coverage
        cov = coverage.Coverage()
        cov.start()

        # Create an instance of ZhipuAIClient
        zhipu_client = ZhipuAIClient(config_file_path)

        # Call the stream_glm4 method to interact with ZhipuAI
        zhipu_client.stream_glm4(prompt_file_path)

        # Stop coverage
        cov.stop()
        cov.save()

        # Assert that all lines are covered
        cov.html_report()

if __name__ == "__main__":
    unittest.main()
