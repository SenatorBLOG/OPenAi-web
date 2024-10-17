import time
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a japanese haiku about love in japaanese."
        }
    ],
    max_tokens=20,
    temperature=0.85,
    top_p=0.95,
    frequency_penalty=0.1,  # Discourage the model from repeating itself
    presence_penalty=0.6 
)

print(completion.choices[0].message)