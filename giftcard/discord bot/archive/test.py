import discord
from discord.ext import commands


TOKEN = 'MTEyMDMyODg5MTc5NDQ1NjYxNg.GL8XfI.zbJJzHrn7tE_3tlcNiCOgsaJDYqDreqtl7Nxk8'


intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def read_messages(ctx, channel_id: int):
    channel = bot.get_channel(channel_id)
    async for message in channel.history(limit=100):
        print(f'{message.author}: {message.content}')

bot.run(TOKEN)
