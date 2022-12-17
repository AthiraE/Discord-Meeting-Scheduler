import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use")
    print("-----------------------------")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hello, i am the Trial Bot")

client.run('MTA1MTAxMzMzNzU0ODMyOTA1Mg.Geanwc.pwxdkDacvksKpjhpgbg39eMrNiLNyJonZGFltw')


     
