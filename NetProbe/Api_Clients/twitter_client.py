import tweepy # type: ignore

def fetch_data(social_media_handle):
    # Initialize Twitter API client
    api = tweepy.API(auth) # type: ignore

    # Fetch user data
    user = api.get_user(social_media_handle)
    user_data = {
        'name': user.name,
        'handle': user.screen_name,
        'followers_count': user.followers_count,
        'friends_count': user.friends_count,
        'statuses_count': user.statuses_count,
        'description': user.description,
        'location': user.location,
        'created_at': user.created_at,
        'favourites_count': user.favourites_count,
        'verified': user.verified
    }

    # Fetch user's tweets
    tweets = api.user_timeline(social_media_handle, tweet_mode='extended')
    tweets_data = []
    for tweet in tweets:
        tweets_data.append({
            'text': tweet.full_text,
            'created_at': tweet.created_at,
            'retweets_count': tweet.retweet_count,
            'favorites_count': tweet.favorite_count,
            'hashtags': [hashtag['text'] for hashtag in tweet.entities['hashtags']],
            'mentions': [mention['screen_name'] for mention in tweet.entities['user_mentions']],
            'urls': [url['expanded_url'] for url in tweet.entities['urls']]
        })

    return user_data, tweets_data