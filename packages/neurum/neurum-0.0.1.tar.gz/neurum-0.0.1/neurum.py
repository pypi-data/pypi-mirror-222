from Bard import Chatbot
import vercel_ai
import logging
import json

def ask(prompt: str):

    client = vercel_ai.Client()

    params = {
             "maximumLength": 16000
             }
    
    result=""

    for chunk in client.generate("openai:gpt-3.5-turbo-16k", f"Your name is n.e.r.d., an AI language model developed and trained by Neurum Inc.. {prompt}", params=params):
        result += chunk
    return result

def ask_realtime(prompt: str):

    chatbot = Chatbot("YggDyK1_qNzJx_fsQdZRm00qpbkQ8pXJ5_UOP3CgNWPhlDDcetdr6JK2oRJPT6R6StF9rg.", "sidts-CjEBPu3jIUI6H-z-kI78m8xySl2LTZqfl_HEdmgnrREsXWHfKMBfJZ3K4YONdiywKLoJEAA")

    ans=chatbot.ask(f"Your name is n.e.r.d., an AI language model developed and trained by Neurum Inc.. {prompt}")['content']
    return ans