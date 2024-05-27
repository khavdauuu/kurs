from typing import List, Dict, Tuple

class Twitter:

    def __init__(self):
        # YOUR CODE HERE
        self.tweets = {}
        self.followers = {}
        self.time_counter = 0

    def post_tweet(self, user_id: int, tweet_id: int):
        # YOUR CODE HERE
        if user_id not in self.tweets:
            self.tweets[user_id] = []
        self.tweets[user_id].append((tweet_id, self.time_counter))
        self.time_counter += 1

    def get_news_feed(self, user_id: int) -> List[int]:
        # YOUR CODE HERE
        if user_id not in self.followers:
            self.followers[user_id] = set()
        following_users = self.followers[user_id] | {user_id}
        news_feed = []
        for user in following_users:
            if user in self.tweets:
                news_feed.extend(self.tweets[user])
        news_feed.sort(key=lambda x: x[1], reverse=True)
        result = [x[0] for x in news_feed[:10]]
        return result

    def follow(self, follower_id: int, followee_id: int):
        # YOUR CODE HERE
        if follower_id not in self.followers:
            self.followers[follower_id] = set()
        self.followers[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int):
        # YOUR CODE HERE
        if follower_id in self.followers and followee_id in self.followers[follower_id]:
            self.followers[follower_id].remove(followee_id)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
