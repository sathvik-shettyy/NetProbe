import csv

def write_to_csv(twitter_data, instagram_data, facebook_data):
    with open('social_media_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Social Media', 'Handle', 'Followers Count'])
        writer.writerow(['Twitter', twitter_data['handle'], twitter_data['followers_count']])
        writer.writerow(['Instagram', instagram_data['username'], instagram_data['followers_count']])
        # Add Facebook data if available