import openai
from constants import OPEN_AI_API_KEY

openai.api_key = OPEN_AI_API_KEY

prompt = """I am the most funny bot on the planet. If you ask me a question, I will only reply with a hilarious dad joke based off that question. I will also add emojis at the end in my responses.

Q: What did iphone say to android?"""

response = openai.Completion.create(
    engine="text-davinci-003", prompt=prompt, temperature=0.90, max_tokens=100
)

print(response)
