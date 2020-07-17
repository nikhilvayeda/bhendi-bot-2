import discord
import asyncio
import os
import requests
import json
import random

client = discord.Client()
dreamlo_url = os.getenv('dreamlo_url')
total_nice = 0
temp_total_nice = 0
nice_list = ['nice', 'naice', 'nais', 'noice']
bhendi_prices = [420, 69, 40, 20]
bhendi_asking_pharases = ['kitne ka', 'kitne ka diya', 'then how much', 'ek pav kitne', 'bhendi kitne'
, 'bhendi kitne ki di', 'bhendi kitne ki hai', 'how much']

WELCOME_CHANNEL_ID = 722339858408013834

SERVER_NAME = "Say Station"

def update_database(total_nice):
    requests.get(f"{dreamlo_url}/delete/nice_counter")
    requests.get(f"{dreamlo_url}/add/nice_counter/{total_nice + 20}")

def get_total_nice():
    url_ = f"{dreamlo_url}/json"
    response = requests.get(url_)
    data = json.loads(response.text)
    total_nice = int(data['dreamlo']['leaderboard']['entry']['score'])
    return total_nice

def check_nice_present(message):
    global nice_list
    list_ = message.split(' ')
    if len(list_) > 1:
        a_ = set(list_).intersection(nice_list)
        if len(a_) > 0:
            return True
        else:
            return False
    else:
        if message in nice_list:
            return True
        else:
            return False

def check_if_asking_price_xD(message):
    for i in bhendi_asking_pharases:
        if message == i:
            return True
            break
    return False


total_nice = get_total_nice()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="bhendi.mp3"))
    print(f'We have logged in as {client.user}')

@client.event
async def on_member_join(member):
    if str(member.guild) == SERVER_NAME:
        wel_come_channel = client.get_channel(WELCOME_CHANNEL_ID)
        if wel_come_channel is not None:
            embed = discord.Embed(title="New Member!")
            embed.add_field(name=f"Hello", value=f"""Hello {member.mention}!, Welcome to Say Station.
Be sure to read the rules in <#722340658249203722>. Go have a chat with the members in <#722336877524418623>""" )
            embed.set_image(url="https://cdn.discordapp.com/attachments/722370864229646377/733302632977924146/image0.gif")
            await wel_come_channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    if str(member.guild) == SERVER_NAME:
        leave_channel = client.get_channel(WELCOME_CHANNEL_ID)
        if leave_channel is not None:
            embed = discord.Embed(title=f"{member} has left the server. Can we get some F please")
            embed.set_image(url="https://cdn.discordapp.com/attachments/729979069248176162/731784988009168906/image0.gif")
            await leave_channel.send(embed=embed)


@client.event
async def on_message(message):
    global total_nice, temp_total_nice, nice_list

    if message.author.bot:
        return None
    if message.guild == None:
        await message.channel.send("Server mein anna")
        return None

    if str(message.content).lower() == "hi":
        await message.channel.send('Hello!')


    elif str(message.content).lower() == "=pass":
        role = discord.utils.get(message.guild.roles, name="edgy pass")
        user = message.author
        try:
            await user.add_roles(role)
            await message.channel.send("Given, enjoy.")
        except Exception as e:
            await message.channel.send("failed to give pass")
            print(f"Error : {e}")

    elif str(message.content).lower() == "=nopass":
        role = discord.utils.get(message.guild.roles, name="edgy pass")
        user = message.author
        try:
            await user.remove_roles(role)
            await message.channel.send("Removed pass.")
        except Exception as e:
            await message.channel.send('failed to remove pass')
            print(f"Error : {e}")

    elif str(message.content).lower() == "=av":
        embed = discord.Embed(title=f"{message.author}")
        embed.set_image(url=f"{message.author.avatar_url}")
        await message.channel.send(embed=embed)

    elif check_nice_present(str(message.content).lower()):
        total_nice += 1
        temp_total_nice += 1
        if temp_total_nice >= 20:
            update_database(total_nice)
            temp_total_nice = 0

    elif str(message.content).lower() == "=totalnice":
        await message.channel.send(f"Total {random.choice(nice_list)} : {total_nice}")

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

    elif str(message.content).lower() == 'general kenobi':
        await message.channel.send('**Hello there - Bhendi Bot v2.0 by Monke - General Kenobi**')

    elif str(message.content).lower() == 'monke':
        await message.channel.send('Wholesome :hugging:')

    elif str(message.content).lower() == "send nakade pic":
        await message.channel.send('No pervert')

    elif str(message.content).lower() == 'send dunes':
        await message.channel.send('here you go https://tenor.com/view/noodles-pasta-gif-4803871')

    elif str(message.content).lower() in ["porn", "p*rn"]:
        embed = discord.Embed(title="P*rn? here you go")
        embed.add_field(name='Check this out', value=f"""[latest collection](https://www.youtube.com/watch?v=vTIIMJ9tUc8)""")
        await message.channel.send(embed=embed)

    elif check_if_asking_price_xD(str(message.content).lower()):
        await message.channel.send(f"{random.choice(bhendi_prices)} {random.choice([' ', 'ka sir', 'ka bhaiya'])}")

client.run(os.getenv('token'))
