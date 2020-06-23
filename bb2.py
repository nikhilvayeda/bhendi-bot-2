import praw
import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Bhendi.mp3"))
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if str(message.content).lower().find('hi') != -1:
        await message.channel.send('Hello!')

    elif str(message.content).lower().find('ooo') != -1:
        await message.channel.send('Bhendi, bhendi!')

    elif str(message.content).lower().find("hello") != -1:
        await message.channel.send('Hi!')

    elif str(message.content).lower().find('-top') != -1:
        await message.channel.send(f"""**_Click the link to see the top members in Sai Station discord_** https://arcanebot.xyz/leaderboard/722336877524418620""")

    elif str(message.content).lower().find('fuck haters') != -1:
        await message.channel.send('Ab Saiman ki baari hai')

    elif str(message.content).lower().find('yalgaar hoe') != -1:
        await message.channel.send('Hoes mad :flushed:')

    elif str(message.content).lower().find('carry tera baap hai') != -1:
        await message.channel.send('Ok mom')

    elif str(message.content).lower().find('kurry tera baap hai') != 1:
        await message.channel.send('Ok mom')

    elif str(message.content).lower().find('curry bhoi tera baap hai') != -1:
        await message.channel.send('Ok mom')

    elif str(message.content).lower().find('curry tera baap hai') != -1:
        await message.channel.send('Ok mom')

    elif str(message.content).lower().find('keri tera baap hai') != -1:
        await message.channel.send('Ok mom https://tenor.com/view/carryminati-ajey-nagar-indian-you-tuber-carryminati-roast-carry-gif-17312966')

    elif str(message.content).lower()[:3] != 'six':
        await message.channel.send('Teri shaadi fix :joy:')

    elif str(message.content).lower()[:6] == 'pencil':
        await message.channel.send('Teri shaadi cancel :joy:')

    elif str(message.content).lower().find('ok mom') != -1:
        await message.channel.send('Wait thats illegal')

    elif str(message.content).lower().find('i wanna kill myself') != -1:
        await message.channel.send('**Dont do it you have more to accomplish suicide help line India 091529 87821**')

    elif str(message.content).lower()[:5] == 'uh oh':
        await message.channel.send('Stinky')

    elif str(message.content).lower().find('bruh') != -1:
        await message.channel.send('Ok obama')

    elif str(message.content).lower()[:3] == 'sex':
        await message.channel.send('When?')

    elif str(message.content).lower().find('general kenobi') != -1:
        await message.channel.send('**Hello there - Bhendi Bot v2.0 by Monke - General Kenobi**')

    elif str(message.content).lower().find('monke') != -1:
        await message.channel.send('Monke seks :flushed:')

    elif str(message.content).lower().find("send nakade pic") != -1:
        await message.channel.send('No pervert')

    elif str(message.content).lower().find('send dunes') != -1:
        await message.channel.send('here you go https://tenor.com/view/noodles-pasta-gif-4803871')

client.run(os.getenv('token'))
