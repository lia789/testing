
"""
import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('MTEyMDM0NTY4ODM4ODE1NzQ3MQ.Gm_yGM.pzmDsTTHSDOVgj_k59vJs-BRSZ0KdVWOHXY8Vo')
"""


# import discord
# from discord.ext import commands


# TOKEN = 'MTEyMDM0NTY4ODM4ODE1NzQ3MQ.Gm_yGM.pzmDsTTHSDOVgj_k59vJs-BRSZ0KdVWOHXY8Vo'


# intents = discord.Intents.default()
# intents.messages = True

# bot = commands.Bot(command_prefix='!', intents=intents)


# @bot.event
# async def on_ready():
#     print(f'{bot.user} has connected to Discord!')


# @bot.command()
# async def read_messages(ctx, channel_id: int):
#     channel = bot.get_channel(channel_id)
#     async for message in channel.history(limit=100):
#         print(f'{message.author}: {message.content}')

# bot.run(TOKEN)


# import discord
# from discord.ext import commands

# intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False

# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot = commands.Bot(command_prefix='!', intents=intents)


# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

#     # Fetches the guild (server) you want to retrieve channels from
#     ID = int("1120209522036838412")
#     guild = bot.get_guild(ID)  # Replace with your guild ID

#     if guild:
#         print('Channels in the server:')
#         for channel in guild.channels:
#             print(channel.name)
#     else:
#         print('Guild not found.')

# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot.run('MTEyMDM0NTY4ODM4ODE1NzQ3MQ.Gm_yGM.pzmDsTTHSDOVgj_k59vJs-BRSZ0KdVWOHXY8Vo')


# import discord
# from discord.ext import commands

# intents = discord.Intents.default()
# intents.typing = False
# intents.presences = False

# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot = commands.Bot(command_prefix='!', intents=intents)

# @bot.event
# async def on_ready():
#     print(f'Logged in as {bot.user.name}')

#     # Replace 'YOUR_CHANNEL_ID' with the ID of the channel you want to retrieve messages from
#     ID = int("1120209779726487613")
#     channel = bot.get_channel(ID)

#     if channel:
#         print(f'Messages in #{channel.name}:')

#         async for message in channel.history(limit=None):
#             print(message.content)
#     else:
#         print('Channel not found.')

# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot.run('MTEyMDM0NTY4ODM4ODE1NzQ3MQ.Gm_yGM.pzmDsTTHSDOVgj_k59vJs-BRSZ0KdVWOHXY8Vo')


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

            embed = discord.Embed(
                title="PRICE ALERT",
                description="The price is below 5",
                color=discord.Color.red()
            )
            embed.set_footer(text="Price notification")
            embed.set_thumbnail(url="https://images.unsplash.com/photo-1536972795217-00f0b4587844?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80")
            await channel.send(embed=embed)

            message = "PRICE IS BELOW 10"
            # await channel.send(message)
            print("===== Message send ======")
    else:
        print('Channel not found.')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTEyMDM0NTY4ODM4ODE1NzQ3MQ.Gm_yGM.pzmDsTTHSDOVgj_k59vJs-BRSZ0KdVWOHXY8Vo')
