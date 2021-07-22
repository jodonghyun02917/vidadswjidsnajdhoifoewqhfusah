import discord
import asyncio
import datetime as dt
import os
client = discord.Client()


f = open("급식.txt", 'r')
y = f.read()
f.close()

@client.event
async def on_ready():
    print("bot ready!")
    print(client.user)
    print("=========================")
    


i = 1
async def a():
    await client.wait_until_ready()
    channel = client.get_channel(866887465172336650)
    while not client.is_closed():
        global i, x
        f = open(f"7_{i}.txt", 'r')
        x = f.read()
        f.close()
        await channel.send("```"+x+"```")
        i += 1
        await asyncio.sleep(10)
@client.event
async def on_message(message): #사용자가 메시지를 입력했을 때
    if message.content == "!급식":
        await message.channel.send("```"+x+"```")

        
client.loop.create_task(a())
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
