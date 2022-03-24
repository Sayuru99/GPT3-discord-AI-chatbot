import discord
import os
import keep_alive
from discord.ext import commands
import OpenAi
intents = discord.Intents().all()
client = commands.Bot(command_prefix="!")

BOT_TOKEN = os.getenv("BOT_TOKEN")

@client.event
async def on_ready():
    print("ohhh who wake up the Kanthiii")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Listening(name='Monsters by Ruelle', url='https://www.youtube.com/watch?v=l7hHeZa3BYU'))

responses = 0
list_user = []

@client.event
async def on_message(message):
    if message.channel.id == message.author.dm_channel.id: # dm only
        #await message.channel.send('ping')
        chat_log = ""
        list_user.append(message.author.id)
        question = message.content
        answer = OpenAi.ask(question, chat_log)
        chat_log = OpenAi.append_interaction_to_chat_log(question, answer,chat_log)
        await message.channel.send(answer)
        f = open("log_user.txt", "w")
        for it in list_user:
        	f.write("%i\n" % it)
        f.close()

@client.command()
@commands.is_owner()
async def shutdown(context):
    exit()


keep_alive.keep_alive()
client.run(BOT_TOKEN)