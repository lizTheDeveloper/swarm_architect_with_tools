import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

async def generate_report_to_channel(report_channel_id, summary):
    report_channel = bot.get_channel(report_channel_id)
    if report_channel:
        await report_channel.send(summary)
    else:
        print(f'Could not find report channel with ID {report_channel_id}')

def generate_report(summary, report_channel_id):
    bot.loop.create_task(generate_report_to_channel(report_channel_id, summary))
    bot.run()