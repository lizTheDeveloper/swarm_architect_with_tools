import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Command listener bot')

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user.name}')

@bot.command()
async def greet(ctx):
    await ctx.send('Hello! I am the bot that listens for commands.')

def command_listener(prefix):
    bot.command_prefix = prefix
    bot.run()