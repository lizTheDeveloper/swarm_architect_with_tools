import discord
from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline('summarization')

bot = discord.Client()

async def summarize_channel(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        messages = await channel.history(limit=100).flatten()
        conversation = '\n'.join([message.content for message in messages])
        summary = summarizer(conversation, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    else:
        return 'No messages found or channel does not exist.'

def summarize_conversation(channel_id):
    return bot.loop.run_until_complete(summarize_channel(channel_id))