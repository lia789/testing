import re
import time

# Selenium library
from parsel import Selector
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Discord library
import discord
from discord.ext import commands



# Discord Token and Client ID Replace with environment variable
CHANNEL_ID = int("1120209779726487613")
TOKEN = "MTEyMDM0NTY4ODM4ODE1NzQ3MQ.Gm_yGM.pzmDsTTHSDOVgj_k59vJs-BRSZ0KdVWOHXY8Vo"


# Selenium driver setup code
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Sending request
driver.get('https://streamelements.com/casinodaddy/store/')
time.sleep(5)


# Html content 
html = driver.page_source
response = Selector(text=html)

_250_git_card_quantity = response.xpath("//h2[@title='Gamdom $250 Gift Card']/..//p[@class='public item-quantity-left']/span/text()").get()
_100_git_card_quantity = response.xpath("//h2[@title='Gamdom $100 Gift Card']/..//p[@class='public item-quantity-left']/span/text()").get()
_50_git_card_quantity = response.xpath("//h2[@title='Gamdom $50 Gift Card']/..//p[@class='public item-quantity-left']/span/text()").get()
_25_git_card_quantity = response.xpath("//h2[@title='Gamdom $25 Gift Card']/..//p[@class='public item-quantity-left']/span/text()").get()
_10_git_card_quantity = response.xpath("//h2[@title='Gamdom $10 Gift Card']/..//p[@class='public item-quantity-left']/span/text()").get()



# Data cleaning code
_25_git_card_quantity = re.findall(r'\d+', _25_git_card_quantity)
_25_git_card_quantity = int(''.join(_25_git_card_quantity))





if _25_git_card_quantity < 10:

    # Discord setup code
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    bot = commands.Bot(command_prefix='!', intents=intents)


    # Discord notification code
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

        # Replace 'YOUR_CHANNEL_ID' with the ID of the channel you want to send the message to
        channel = bot.get_channel(CHANNEL_ID)

        if channel:

            # Should be replace with client requirements
            embed = discord.Embed(
                title="Gamdom Gift Cards Restocked!",
                url="https://streamelements.com/casinodaddy/store/",
                description="Good news! The Gamdom gift cards are back in stock on the store. Hurry, grab yours before they sell out again!",
                color=0xf91010
                )
            embed.set_thumbnail(url="https://i.postimg.cc/9Q4sKqvr/ambulance-lights.png")
            embed.add_field(name="250$ countity:", value=_250_git_card_quantity, inline=True)
            embed.add_field(name="100$ countity:  ", value=_100_git_card_quantity, inline=False)
            embed.add_field(name="50$ countity:  ", value=_50_git_card_quantity, inline=False)
            embed.add_field(name="25$ countity:  ", value=_25_git_card_quantity, inline=False)
            embed.add_field(name="10$ countity:  ", value=_10_git_card_quantity, inline=False)

            

        
            await channel.purge(limit=None)
            await channel.send(embed=embed)
            print("===== Message send ======")
        else:
            print('Channel not found.')
        
        await bot.close()
    
    # Run the Discord bot 
    bot.run(TOKEN)






























