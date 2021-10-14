# app.py - Discord bot functionality
# Arizona State University - Poly
# Childless Millenials

# Imports
import os
from dotenv import load_dotenv
from discord.ext import commands
from lib.reddit import get_random_image


# Loads .env file for API keys
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Creates bot instance
bot = commands.Bot(command_prefix='!')

# Event when connection is completed
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Discord call which posts a random submission of dog
@bot.command(name="dog", help="Displays a good boy (or girl)")
async def dog(ctx):
    image_link = await get_random_image("rarepuppers")
    await ctx.send(image_link)

# Command which grabs a random image from the subreddit supplied
# Usage: !random <subreddit>
# Example: !random memes
@bot.command(name="random", help="Displays a random image from the given subreddit.")
async def dog(ctx, arg):
    image_link = await get_random_image(arg)
    await ctx.send(image_link)

# Execute bot
bot.run(TOKEN)
