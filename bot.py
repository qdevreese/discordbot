import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("BOT IS WORKING CORRECTLY")
    await client.change_presence(activity=discord.Game(name="Fucking shit up big time"))

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

client.run('NzQyOTc2OTExNTc5MjgzNDg2.XzN9Kw.J7hTB8NBROLqW5JDRRVWkKP6UWo')
