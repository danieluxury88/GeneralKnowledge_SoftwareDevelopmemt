import os
from dotenv import load_dotenv

load_dotenv()

api = os.getenv("GPT_API_KEY")
print(api)