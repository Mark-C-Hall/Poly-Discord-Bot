# app.py - Discord bot functionality
# Arizona State University - Poly
# Childless Millenials

# Imports
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncpraw


# Loads .env file for API keys
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')


# Creates bot instance
bot = commands.Bot(command_prefix='!')


# Initialization Event
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# Chat command for showing a random dog from Reddit
reddit = asyncpraw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Discord call which posts a random submission
@bot.command(name="dog", help="Displays a good boy (or girl)")
async def dog(ctx):
    # Loops through random submissions until a jpg is found
    is_image = False
    while not (is_image):
        subreddit = await reddit.subreddit('rarepuppers')
        submission = await subreddit.random()
        is_image = submission.url.endswith(".jpg")

    await ctx.send(submission.url)


# Execute bot
bot.run(TOKEN)