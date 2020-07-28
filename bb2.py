import discord
import requests
import json
import random
from discord.ext import tasks, commands
import praw
from VARIABLES_ import *
from FUNCTIONS_ import *
from RANDOM_REPLIES import RandomReply

client = commands.Bot(command_prefix="=")

total_counteded = {"bruh" : get_total_word_counted(0), "nice" : get_total_word_counted(1)}


@client.event
async def on_ready():

    update_memes()
    send_meme.start()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="bhendi.mp3"))
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):

    if str(member.guild) == SERVER_NAME:
        wel_come_channel = client.get_channel(WELCOME_CHANNEL_ID)
        if wel_come_channel is not None:
            _total_member = 0
            for m in member.guild.members:
                if not m.bot:
                    _total_member += 1

            embed = discord.Embed(title="New Member!")
            embed.add_field(name=f"Hello", value=f"""Hello {member.mention}!({member}), Welcome to Say Station. \n
                            Be sure to read the rules in <#722340658249203722>. Go have a chat with the members in <#722336877524418623>""" )
            embed.add_field(name="Member Count", value=f"#{_total_member + 1} member")
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
    global bhendi_prices

    if message.author.bot:
        return None

    if message.guild == None:
        await message.channel.send("Server mein anna")
        return None

    reply = RandomReply(str(message.content))

    if reply != None:
        await message.channel.send(reply)

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


    elif check_if_asking_price_xD(str(message.content).lower()):
        await message.channel.send(f"{random.choice(bhendi_prices)} {random.choice([' ', 'ka sir', 'ka bhaiya'])}")


    # Counters
    elif check_counted_words_present(str(message.content)) != None:
        index_of_word_counted = check_counted_words_present(str(message.content))
        word_counted = counted_words[index_of_word_counted]
        temp_total_counteded[word_counted] += 1
        total_counteded[word_counted] += 1


        if temp_total_counteded[word_counted] == 20:
            update_database(index_of_word_counted, total_counteded[counted_words[index_of_word_counted]])
            temp_total_counteded[word_counted] = 0

    elif str(message.content)[:6] == "=total":
        if str(message.content)[6:] in counted_words:
            await message.channel.send(f"total {str(message.content[6:])} : {total_counteded[str(message.content)[6:]]}")

    elif str(message.content).lower()[:7] == "=repeat":
        if len(str(message.content)[7:]) > 0:

            if len(message.role_mentions) > 0 or "@everyone" in str(message.content) or "@here" in str(message.content):
                embed = discord.Embed(title=f" ")
                embed.add_field(name=">_<", value=f"{message.content[7:]}")
                await message.channel.send(embed=embed)

            else:
                await message.channel.send(message.content[7:])


# MEMES
res = praw.Reddit(client_id=REDDIT_KEY, client_secret=REDDIT_SECRET,
                   user_agent="bhendi")

ALL_MEMES = []
MEME_COUNT = 0
@tasks.loop(seconds=600)
async def send_meme():
    global ALL_MEMES, MEME_COUNT
    if MEME_COUNT >= 144:
        update_memes()
    channel_ = client.get_channel(REDDIT_MEMES_ID)
    _current_meme = ALL_MEMES[MEME_COUNT]
    MEME_COUNT += 1
    embed = discord.Embed(title="Reddit Review")
    embed.add_field(name='Author', value=f"[{_current_meme['author']}]({_current_meme['author_profile']})")
    embed.add_field(name="Post", value=f"[{_current_meme['post_title']}]({_current_meme['post_link']})")
    embed.set_image(url=_current_meme['image_url'])
    if channel_ != None:
        await channel_.send(embed=embed)

@send_meme.before_loop
async def before_send_meme():
    await client.wait_until_ready()

def update_memes():
    global ALL_MEMES, MEME_COUNT
    for i in res.subreddit('SaimanSays').hot(limit=145):
        _meme = {'author' : i.author, 'author_profile' : f"https://www.reddit.com/u/{i.author}"
        , "image_url" : i.url,"post_title" : i.title,
        "post_link" : f"https://reddit.com{i.permalink}"}

        ALL_MEMES.append(_meme)
    MEME_COUNT = 0

client.run(TOKEN)
