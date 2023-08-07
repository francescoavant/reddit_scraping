import praw
import json
from connection import *
from flask_restx import Resource, Namespace
from datetime import datetime
from util import *
import uuid

api= Namespace('reddit_scraping')


@api.route('/reddit/post/<subreddit_name>')
class Reddit(Resource):
    def get(self, subreddit_name):
        subreddit = reddit.subreddit(subreddit_name)
        top_posts = subreddit.top(limit=10)
        posts_data = []
        for post in top_posts:
            post_data = {
                'title': post.title,
                'score': post.score,
                'id': post.id,
                'url': post.url,
                'comms_num': post.num_comments,
                'created': datetime.utcfromtimestamp(post.created).strftime('%Y-%m-%d %H:%M:%S')
            }
            posts_data.append(post_data)
        #result = save_json(posts_data)
        id = str(uuid.uuid4())
        postfilename= "posts-"+ id +".json"
        with open(postfilename, 'w', encoding='utf8') as f:
                json.dump(posts_data, f, ensure_ascii=False, indent=4)
        Media.media_down(postfilename)
        return ("task completed")

@api.route('/reddit/comments/<path:url>')
class Reddit(Resource):
        def get(self, url):
        #scrape all comments and save to json file 
            submission = reddit.submission(url=url)
            comments_data = []
            for comment in submission.comments.list():
                if isinstance(comment, praw.models.MoreComments):
                    continue
                comment_data = {
                    'author': comment.author.name if comment.author else '[deleted]',
                    'body': comment.body,
                    'score': comment.score,
                    'id': comment.id,
                    'created': datetime.utcfromtimestamp(comment.created).strftime('%Y-%m-%d %H:%M:%S')
                }
                comments_data.append(comment_data)
            # Save comments to a JSON file
            filename= "comments-"+ url.split("/comments/")[1].split("/")[0] +".json"
            with open(filename, 'w', encoding='utf8') as f:
                json.dump(comments_data, f, ensure_ascii=False, indent=4)
            return ("task completed")






