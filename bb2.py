import discord
import asyncio 
import os 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Hi"):
        await message.channel.send('Hello!')
    if message.content.startswith("hi"):
        await message.channel.send('Hello!')
    if message.content.startswith("Ooo"):
        await message.channel.send('Bhendi, bhendi!')
    if message.content.startswith("Hello"):
        await message.channel.send('Hi!')
    if message.content.startswith("hello"):
        await message.channel.send('Hi!')
    elif message.content == "-top":
        await message.channel.send(f"""**_Click the link to see the top members in Sai Station discord_** https://arcanebot.xyz/leaderboard/722336877524418620""")
    if message.content.startswith("Fuck haters"):
        await message.channel.send('Ab Saiman ki baari hai')
    if message.content.startswith("fuck haters"):
        await message.channel.send('Ab Saiman ki baari hai')
    if message.content.startswith("Yalgaar hoe"):
        await message.channel.send('Hoes mad :flushed:')
    if message.content.startswith("yalgaar hoe"):
        await message.channel.send('Hoes mad :flushed:')
    if message.content.startswith('Carry tera baap hai'):
        await message.channel.send('Ok mom')
    if message.content.startswith('carry tera baap hai'):
        await message.channel.send('Ok mom')
    if message.content.startswith('kurry tera baap hai'):
        await message.channel.send('Ok mom')
    if message.content.startswith('curry bhoi tera baap hai'):
        await message.channel.send('Ok mom')
    if message.content.startswith('curry tera baap hai'):
        await message.channel.send('Ok mom')
    if message.content.startswith('keri tera baap hai'):
        await message.channel.send('Ok mom https://tenor.com/view/carryminati-ajey-nagar-indian-you-tuber-carryminati-roast-carry-gif-17312966')
    if message.content.startswith('six'):
        await message.channel.send('Teri shaadi fix :joy:')
    if message.content.startswith('Six'):
        await message.channel.send('Teri shaadi fix :joy:')
    if message.content.startswith('Pencil'):
        await message.channel.send('Teri shaadi cancel :joy:')
    if message.content.startswith('pencil'):
        await message.channel.send('Teri shaadi cancel :joy:')
    if message.content.startswith('Ok mom'):
        await message.channel.send('Wait thats illegal')
    if message.content.startswith('ok mom'):
        await message.channel.send('Wait thats illegal')
    if message.content.startswith('I wanna kill myself'):
        await message.channel.send('**Dont do it you have more to accomplish suicide help line India 091529 87821**')
    if message.content.startswith('i wanna kill myself'):
        await message.channel.send('**Dont do it you have more to accomplish suicide help line India 091529 87821**')
    if message.content.startswith('uh oh'):
        await message.channel.send('Stinky')
    if message.content.startswith('Uh oh'):
        await message.channel.send('Stinky')
    if message.content.startswith('Bruh'):
        await message.channel.send('Ok obama')
    if message.content.startswith('bruh'):
        await message.channel.send('Ok obama')
    if message.content.startswith('Sex'):
        await message.channel.send('When?')
    if message.content.startswith('sex'):
        await message.channel.send('When?')
    if message.content.startswith('General kenobi'):
        await message.channel.send('**Hello there - Bhendi Bot v2.0 by Monke - General Kenobi**')
    if message.content.startswith('general kenobi'):
        await message.channel.send('**Hello there - Bhendi Bot v2.0 by Monke - General Kenobi**')
    if message.content.startswith('Monke'):
        await message.channel.send('Monke seks :flushed:')
    if message.content.startswith('monke'):
        await message.channel.send('Monke seks :flushed:')
    if message.content.startswith('Send nakade pic'):
        await message.channel.send('No pervert')
    if message.content.startswith('send nakade pic'):
        await message.channel.send('No pervert')
    if message.content.startswith('Send dunes'):
        await message.channel.send('Here you go https://tenor.com/view/noodles-pasta-gif-4803871')
    if message.content.startswith('send dunes'):
        await message.channel.send('here you go https://tenor.com/view/noodles-pasta-gif-4803871')


client.run(os.getenv('token'))
