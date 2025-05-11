"""
Tutorial Source:
    https://huggingface.co/docs/transformers/en/tasks/sequence_classification
"""
import os
from dotenv import load_dotenv
from huggingface_hub import login
load_dotenv()

# Configurations
token = os.getenv("HF_TOKEN")
login(token=token)
