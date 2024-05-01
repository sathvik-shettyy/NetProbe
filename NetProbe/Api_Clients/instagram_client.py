import instaloader # type: ignore

def fetch_data(social_media_handle):
    # Initialize Instagram API client
    loader = instaloader.Instaloader()

    # Fetch user data
    user = loader.get_profile(social_media_handle)
    user_data = {
        'username': user.username,
        'full_name': user.full_name,
        'followers_count': user.followers,
        'followees_count': user.followees,
        'posts_count': user.media_count,
        'biography': user.biography,
        'is_private': user.is_private,
        'is_verified': user.is_verified
    }

    # Fetch user's posts
    posts = user.get_posts()
    posts_data = []
    for post in posts:
        posts_data.append({
            'caption': post.caption,
            'like_count': post.likes,
            'comment_count': post.comments,
            'created_at': post.date_local,
            'image_url': post.url
        })

    return user_data, posts_data