# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = CHATGPT_API_KEY

primer = "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: January 2022 Current date: March 2023"
result = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": primer},
        {"role": "user", "content": "Can you list the 20 most appreciated mid level free certificates in Computer Science industry?"},
        # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        # {"role": "user", "content": "Where was it played?"}
        # {"role": "assistant", "content": "One example is edx CS50."},

    ]
)
print(type(result))

print(result)