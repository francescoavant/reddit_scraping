import praw
import os
from dotenv import load_dotenv
load_dotenv()
#Reddit instance
reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    user_agent= os.environ["USER_AGENT"],
    rate_limit_seconds=500,
)