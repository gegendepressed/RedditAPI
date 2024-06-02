from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import praw
from dotenv import load_dotenv
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()


reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    ratelimit_seconds=300
)

@app.get("/{subreddit}" , status_code=201)
def fetch(subreddit: str):
    try:
        submission = reddit.subreddit(subreddit).random()
        return { 
                "title": submission.title,
                "description": submission.selftext,
                "url" : submission.url,
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail="Subreddit not found")

    
