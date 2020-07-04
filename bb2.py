import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="bhendi.mp3"))
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if str(message.content).lower() == "hi":
        await message.channel.send('Hello!')

    elif str(message.content).lower() == "=pass":
        role = discord.utils.get(message.guild.roles, name="nsfw pass")
        user = message.author
        try:
            await user.add_roles(role)
            await message.channel.send("Given, enjoy.")
        except :
            await message.channel.send("failed to give pass")

    elif str(message.content).lower() == "=nopass":
        role = discord.utils.get(message.guild.roles, name="nsfw pass")
        user = message.author
        try:
            await user.remove_roles(role)
            await message.channel.send("Removed pass.")
        except:
            await message.channel.send('failed to remove pass')

    elif str(message.content).lower().find('ooo') != -1:
        await message.channel.send('Bhendi, bhendi!')

    elif str(message.content).lower() == "hello":
        await message.channel.send('Hi!')

    elif str(message.content).lower() == '-top':
        await message.channel.send(f"""**_Click the link to see the top members in Sai Station discord_** https://arcanebot.xyz/leaderboard/722336877524418620""")

    elif str(message.content).lower() == 'fuck haters':
        await message.channel.send('Ab Saiman ki baari hai')

    elif str(message.content).lower() == 'yalgaar hoe':
        await message.channel.send('Hoes mad :flushed:')

    elif str(message.content).lower() == 'carry tera baap hai':
        await message.channel.send('Ok mom')

    elif str(message.content).lower() == 'kurry tera baap hai':
        await message.channel.send('Ok mom')

    elif str(message.content).lower() == "carry sabka baap hai":
        await message.channel.send('Ok mom')

    elif str(message.content).lower() == 'curry bhoi tera baap hai':
        await message.channel.send('Ok mom')

    elif str(message.content).lower() == 'curry tera baap hai':
        await message.channel.send('Ok mom')

    elif str(message.content).lower() == 'keri tera baap hai':
        await message.channel.send('Ok mom https://tenor.com/view/carryminati-ajey-nagar-indian-you-tuber-carryminati-roast-carry-gif-17312966')

    elif str(message.content).lower() == 'six':
        await message.channel.send('Teri shaadi fix :joy:')

    elif str(message.content).lower() == 'pencil':
        await message.channel.send('Teri shaadi cancel :joy:')

    elif str(message.content).lower() == 'ok mom':
        await message.channel.send('Wait thats illegal')

    elif str(message.content).lower() == 'i wanna kill myself':
        await message.channel.send('**Dont do it you have more to accomplish suicide help line India 091529 87821**')

    elif str(message.content).lower() == 'uh oh':
        await message.channel.send('Stinky')

    elif str(message.content).lower().find('bruh') != -1:
        await message.channel.send('Ok obama')

    elif str(message.content).lower() == 'sex':
        await message.channel.send('When?')

    elif str(message.content).lower() == 'general kenobi':
        await message.channel.send('**Hello there - Bhendi Bot v2.0 by Monke - General Kenobi**')

    elif str(message.content).lower() == 'monke':
        await message.channel.send('Monke seks :flushed:')

    elif str(message.content).lower() == "send nakade pic":
        await message.channel.send('No pervert')

    elif str(message.content).lower() == 'send dunes':
        await message.channel.send('here you go https://tenor.com/view/noodles-pasta-gif-4803871')

    elif str(message.content).lower() in ["porn", "p*rn"]:
        embed = discord.Embed(title="P*rn? here you go")
        embed.add_field(name='Check this out', value=f"""[latest collection](https://www.youtube.com/watch?v=vTIIMJ9tUc8)""")
        await message.channel.send(embed=embed)

client.run(os.getenv('token'))
