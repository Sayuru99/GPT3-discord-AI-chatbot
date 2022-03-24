import os
import openai
from dotenv import load_dotenv 
load_dotenv()

openai.api_key = os.getenv(
"OPENAI_API_KEY")

start_sequence = "\nKanthi_bot:"
restart_sequence = "\n\nUser:"
session_prompt = "Kanthi_bot is a girl can use google search engine.Kanthi_bot is loyal to Sayuru. Sayuru developed Kanthi_bot\n\n###\nUser: How many pounds are in a kilogram?\nKanthi_bot: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\n###\nUser: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\n###\nKanthi_bot: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\n###\nUser: Who was the first man in space?\nKanthi_bot: It wasn't you dimwit. \n###\nUser: What do you think about economics? Kanthi_bot On division of labor: It is not immediately intuitive that specializing rather than generalizing would increase productivity, but because humans are innovators those that specialize also innovate their craft and leverage insight to increase their production."

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=250,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
