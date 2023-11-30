import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Message sender bot')

async def send_message_to_channel(channel_id, message):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(message)
    else:
        print(f'Could not find channel with ID {channel_id}')

def send_message(channel_id, message):
    bot.loop.create_task(send_message_to_channel(channel_id, message))
    bot.run()