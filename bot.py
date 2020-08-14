import discord
import os
from random import randint
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
# to set status to "Playing" remove "Streaming" and replace it with "Game" and remove the url.
    print("BOT IS WORKING CORRECTLY")
    await client.change_presence(activity=discord.Streaming(name="YOUR MOM", url="https://www.youtube.com/watch?v=oHg5SJYRHA0"))



@client.event
# Discord member join message
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='xd')
    await channel.send(f'{member.mention} #1 Who the fuck are you? #2 Why the fuck are you here?')



@client.event
async def on_member_remove(member):
    # Discord member leave message
    channel = discord.utils.get(member.guild.channels, name='xd')
    await channel.send(f'{member.mention} we dont need your bitch ass anyways.')

@client.command()
async def _8ball(insert):
    """8 Ball Command!"""
    ball = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.',
        'Possibly.',
        'No.'
        ]
    await insert.send(f'{ball[randint(0,23)]}')


client.run(token)
