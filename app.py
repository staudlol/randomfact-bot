import discord
import randfacts

from discord.ext import commands

# Prefix
client = commands.Bot(command_prefix='!')

# Token
TOKEN = "Put your token here"

@client.event
async def on_ready():
    print('Loaded randomfact-bot')

@client.command()
async def randomfact(ctx):
    await ctx.reply(randfacts.get_fact())

client.run(TOKEN)