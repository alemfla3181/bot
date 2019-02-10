import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("zzzzzzzzzzzzzzzz")
    await client.change_presence(game=discord.Game(name='아니 어쩌란건데?', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('!야'):
        await client.send_message(message.channel, " 뭐 이 새기야")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
