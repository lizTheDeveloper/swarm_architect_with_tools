import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_message_delete(message):
    print(f'Message by {message.author.display_name} deleted: {message.content}')

@bot.event
async def on_member_join(member):
    print(f'{member.display_name} has joined the server.')

@bot.event
async def on_member_remove(member):
    print(f'{member.display_name} has left the server.')

def monitor_channel_activity(channel_id):
    # This function is integrated with the bot event listeners
    # Additional functionality will be implemented as required
    bot.run()