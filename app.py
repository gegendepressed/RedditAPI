from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import praw
import random
from dotenv import load_dotenv
import os
from datetime import datetime
import praw.exceptions

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
def fetchrandom(subreddit: str):
    try:
        submission = reddit.subreddit(subreddit).random()
        submission_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%d-%m-%y')        

        return { 
                "title": submission.title,
                "description": submission.selftext,
                "url" : submission.url,
                "date" : submission_date,
        }
    except praw.exceptions.APIException as e:
        raise HTTPException(status_code=500, detail=f"Reddit API error!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred !")

@app.get("/{subreddit}/top/pastweek" , status_code=200)
def fetchtop_week(subreddit):
   try:
        submissions = list(reddit.subreddit(subreddit).top('week', limit=100))
        submission = random.choice(submissions)
        submission_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%d-%m-%y')        
        return {
            "title": submission.title,
            "description": submission.selftext,
            "url": submission.url,
            "date" : submission_date,
        }
   except praw.exceptions.APIException as e:
        raise HTTPException(status_code=500, detail=f"Reddit API error!")
   except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred !")

   
@app.get("/{subreddit}/top/pastmonth" , status_code=200)
def fetchtop_month(subreddit):
   try:
        submissions = list(reddit.subreddit(subreddit).top('month', limit=100))
        submission = random.choice(submissions)
        submission_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%d-%m-%y')        
        return {
            "title": submission.title,
            "description": submission.selftext,
            "url": submission.url,
            "date" : submission_date,
        }
   except praw.exceptions.APIException as e:
        raise HTTPException(status_code=500, detail=f"Reddit API error!")
   except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred !")

   
@app.get("/{subreddit}/top/pastyear" , status_code=200)
def fetchtop_year(subreddit):
   try:
        submissions = list(reddit.subreddit(subreddit).top('year', limit=100))
        submission = random.choice(submissions)
        submission_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%d-%m-%y')        
        return {
            "title": submission.title,
            "description": submission.selftext,
            "url": submission.url,
            "date" : submission_date,
        }
   except praw.exceptions.APIException as e:
        raise HTTPException(status_code=500, detail=f"Reddit API error!")
   except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred !")

@app.get("/{subreddit}/hot" , status_code=200)
def fetchtop_month(subreddit):
   try:
        submissions = list(reddit.subreddit(subreddit).hot(limit=100))
        submission = random.choice(submissions)
        submission_date = datetime.utcfromtimestamp(submission.created_utc).strftime('%d-%m-%y')        
        return {
            "title": submission.title,
            "description": submission.selftext,
            "url": submission.url,
            "date" : submission_date,
        }
   except praw.exceptions.APIException as e:
        raise HTTPException(status_code=500, detail=f"Reddit API error!")
   except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred !")



    

    
