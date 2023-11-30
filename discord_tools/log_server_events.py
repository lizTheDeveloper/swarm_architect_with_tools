import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

async def log_event(event_message, log_channel_id):
    log_channel = bot.get_channel(log_channel_id)
    if log_channel:
        await log_channel.send(event_message)
    else:
        print(f'Could not find log channel with ID {log_channel_id}')

def log_server_events(event, log_channel_id):
    # This function will trigger the logging task
    bot.loop.create_task(log_event(event, log_channel_id))
    bot.run()