import praw
from utils import send_email
import datetime

#daily log
with open('./log.txt','w') as l:
    l.write(str(datetime.datetime.now()))
    l.close()

#obtain the different subreddits
with open('./subreddits.txt','r') as f:
    data = f.read()
subs = data.split('\n')

reddit = praw.Reddit(client_id=YOUR_CLIENT_ID,
                     client_secret=YOUR_CLIENT_SECRET,
                     user_agent=YOUR_USER_AGENT)


body = "Here's the daily roundup: \n\n"
#iterate through the subreddits
for sub in subs:
    if(sub != ''):
        subreddit = reddit.subreddit(sub)
        body += sub+":"+"\n"
        count = 1
        for submission in subreddit.top(limit=5,time_filter = "day"):
            body += str(count) + ". " + str(submission.title) + "\n"
            body += "Post Score: " + str(submission.score) + "\n"
            body += "Url: " + str(submission.url) + "\n"
            count += 1
        body += "\n\n\n"

#finally send the daily email
send_email(<sender email>,<sender password>,<reciever email>,"Your Daily Roundup",body)