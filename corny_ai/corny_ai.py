import openai
import streamlit as st
from constants import OPEN_AI_API_KEY

openai.api_key = st.secrets['OPEN_AI_API_KEY']

def get_corny(prompt:str, temperature:float, max_tokens=100):
    
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, temperature=temperature, max_tokens=max_tokens
    )

    return response

header = prompt = """I am the most funny bot on the planet. If you ask me a question, I will only reply with a hilarious dad joke based off that question. I will also add emojis at the end in my responses.\n\n"""
prompt = "Q: What did iphone say to android?"

if __name__ == "__main__":

    out = get_corny(prompt=header+prompt,
                    temperature=0.76,
                    max_tokens=100)
    print(out['choices'][0]['text'])