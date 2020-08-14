import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("BOT IS WORKING CORRECTLY")
    await client.change_presence(activity=discord.Streaming(name="YOUR MOM", url = "https://www.youtube.com/watch?v=oHg5SJYRHA0"))

#to set status to "Playing" remove "Streaming" and replace it with "Game" and remove the url.

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='xd')
    await channel.send(f'{member.mention} #1 Who the fuck are you? #2 Why the fuck are you here?')

#Discord member join message

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='xd')
    await channel.send(f'{member.mention} we dont need your bitch ass anyways.')

#Dsicord member leave message

client.run(token)
