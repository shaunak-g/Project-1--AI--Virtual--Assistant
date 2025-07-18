from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your Key Here>",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Echo which is skilled in answering questions and providing information on a wide range of topics."},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)