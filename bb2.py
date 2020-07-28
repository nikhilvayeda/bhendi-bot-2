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
DELETED_MESSAGES = []
EDITED_MESSAGES = []

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

            if len(message.role_mentions) > 0 or message.mention_everyone:
                embed = discord.Embed(title=f" ")
                embed.add_field(name=">_<", value=f"{message.content[7:]}")
                await message.channel.send(embed=embed)

            else:
                await message.channel.send(message.content[7:])

    elif str(message.content).lower() == "=deleted":
        embed = discord.Embed(title="__**Last Deleted Messages**__")

        if len(DELETED_MESSAGES) > 0:
            for msg in DELETED_MESSAGES:
                embed.add_field(name=f"By {msg['author']}", value=f'Message : **{msg["message"]}**\n\n')
        else:
            embed.add_field(name="No message was deleted after I woke up", value="¯\\_(ツ)_/¯")

        await message.channel.send(embed=embed)


    elif str(message.content).lower() == "=edited":
        embed = discord.Embed(title="__**Last Edited Messages**__")

        if len(EDITED_MESSAGES) > 0:
            for msg in EDITED_MESSAGES:
                embed.add_field(name=f"by {msg['author']}",
                                value=f"Original Message : {msg['message_before']}\nEdited Message : {msg['message_after']}\n\n")
        else:
            embed.add_field(name="No message was edited after I woke up", value="¯\\_(ツ)_/¯")

        await message.channel.send(embed=embed)

    elif str(message.content).lower() == "=source":
        _msg = f"Here's the repository link, fork the repo, make changes, then create a pull request.\n {REPO_LINK}"
        await message.channel.send(_msg)



@client.event
async def on_raw_message_delete(payload):
    if payload.guild_id == SERVER_ID and not payload.cached_message.author.bot:
        if str(payload.cached_message.content).lower()[:7] == "=repeat":
            if len(str(payload.cached_message.content)[7:]) > 0:
                embed = discord.Embed(title=f"__**=repeat Command Message Deleted**__")
                embed.add_field(name="**Original Message >_< :**", value=f"{payload.cached_message.content}")
                embed.add_field(name="**Author**", value=f"{payload.cached_message.author.mention}")
                await payload.cached_message.channel.send(embed=embed)

        else:
            _msg = {"author" : payload.cached_message.author, "message" : payload.cached_message.content}
            DELETED_MESSAGES.append(_msg)
            if len(DELETED_MESSAGES) > 5:
                del DELETED_MESSAGES[0]

@client.event
async def on_message_edit(before, after):
    if before.guild.id == SERVER_ID and not before.author.bot:

        if str(before.content).lower()[:7] == "=repeat":
            if len(str(before.content)[7:]) > 0:

                embed = discord.Embed(title=f"__**=repeat Command Message Edited**__")
                embed.add_field(name="**Original Message >_< :**", value=f"{before.content}")
                embed.add_field(name="**Edited Message >_< :**", value=f"{after.content}")

                embed.add_field(name="**Author**", value=f"{before.author.mention}")
                await before.channel.send(embed=embed)

        else:
            _msg = {"author" : before.author, "message_before" : before.content,
            "message_after" : after.content }

            EDITED_MESSAGES.append(_msg)

        if len(EDITED_MESSAGES) > 5:
            del EDITED_MESSAGES[0]



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
    for i in res.subreddit('SaimanSays').hot(limit=200):
        if str(i.url).endswith(('.jpg', '.png', '.jpeg', '.gif', '.webp')):
            _meme = {'author' : i.author, 'author_profile' : f"https://www.reddit.com/u/{i.author}"
            , "image_url" : i.url,"post_title" : i.title,
            "post_link" : f"https://reddit.com{i.permalink}"}

            ALL_MEMES.append(_meme)

    MEME_COUNT = 0

client.run(TOKEN)
