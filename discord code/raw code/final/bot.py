import discord
from discord.ext import commands


CHANNEL_ID = int("")
TOKEN = ""


# Discord setup code
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)





@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        price = 5

        if price < 10:
            await channel.purge(limit=None)

            embed = discord.Embed(
                title="PRICE ALERT",
                description="The price is below 5",
                color=discord.Color.red()
            )
            embed.set_footer(text="Price notification")
            embed.set_thumbnail(url="https://images.unsplash.com/photo-1536972795217-00f0b4587844?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80")
            await channel.send(embed=embed)

            
            # await channel.send(message)
            print("===== Message send ======")
    else:
        print('Channel not found.')




bot.run(TOKEN)