import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    # Replace 'YOUR_CHANNEL_ID' with the ID of the channel you want to send the message to
    YOUR_CHANNEL_ID = int("1120209779726487613")
    channel = bot.get_channel(YOUR_CHANNEL_ID)

    if channel:
        price = 5

        if price < 10:
            await channel.purge(limit=None)

            
            # embed = discord.Embed(
            #     title="PRICE ALERT",
            #     description="The price is below 5",
            #     color=discord.Color.red()
            # )
            # embed.set_footer(text="Price notification")
    
            

            embed = discord.Embed(
                title="Gamdom Gift Cards Restocked!",
                url="https://streamelements.com/casinodaddy/store/",
                description="Good news! The Gamdom gift cards are back in stock on the store. Hurry, grab yours before they sell out again!",
                color=0xf91010
                )
            embed.set_thumbnail(url="https://i.postimg.cc/9Q4sKqvr/ambulance-lights.png")
            
            embed.add_field(name="", value="", inline=False)

            
            
            
            
            
            
            await channel.send(embed=embed)








            # await channel.send(message)
            print("===== Message send ======")
    else:
        print('Channel not found.')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTEyMDM0NTY4ODM4ODE1NzQ3MQ.Gm_yGM.pzmDsTTHSDOVgj_k59vJs-BRSZ0KdVWOHXY8Vo')
