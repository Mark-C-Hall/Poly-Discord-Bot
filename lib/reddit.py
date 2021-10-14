# reddit.py
# Runs Reddit requests
# Childless Millenials

# Imports
import os
from dotenv import load_dotenv
import asyncpraw

# Load Env variables
load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')


# Initialize Reddit Object
reddit = asyncpraw.Reddit(client_id=CLIENT_ID,
                          client_secret=CLIENT_SECRET,
                          user_agent=USER_AGENT)


# Helper function which returns a random image from the provided Subreddit
async def get_random_image(board):

    # Loops through random submissions until a jpg is found
    is_image = False
    while not (is_image):
        subreddit = await reddit.subreddit(board)
        submission = await subreddit.random()
        is_image = submission.url.endswith(".jpg")

    return submission.url

