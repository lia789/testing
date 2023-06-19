import discord
from discord.ext import tasks
from parsel import Selector
import requests
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

channel_id = '1120209779726487613'  # replace with your channel ID
bot_token = 'MTEyMDI1MjM0Nzc0Mjk2NTgwMA.Gb7mow.xK8VTlUjxcm39m4j5cgo2KC1OQQk9_Nfxl5qh4'  # replace with your bot token

@client.event
async def on_ready():
    check_price.start()  # start the task when the bot is ready

@tasks.loop(hours=1)
async def check_price():
    channel = client.get_channel(int(channel_id))

    # Fetch the price
    # html = requests.get(url)
    # response = Selector(text=html.text)
    # price = float(response.xpath("//h1/text()").get())

    price = 5

    # Delete all messages in the channel
    await channel.purge()

    # If the price is below 10, send a message
    if price < 10:
        await channel.send('Price is below 10, go and buy')

client.run(bot_token)
