# main.py

from api_clients import twitter_client, instagram_client, facebook_client # type: ignore
from data_storage import database, csv_handler # type: ignore
from data_analysis import data_analyzer

def main():
    # Get user input
    social_media_handle = input("Enter the social media handle you want to investigate: ")

    # Fetch data from social media APIs
    twitter_data = twitter_client.fetch_data(social_media_handle)
    instagram_data = instagram_client.fetch_data(social_media_handle)
    facebook_data = facebook_client.fetch_data(social_media_handle)

    # Store the collected data
    database.store_data(twitter_data, instagram_data, facebook_data)
    csv_handler.write_to_csv(twitter_data, instagram_data, facebook_data)

    # Analyze the data
    data_analyzer.analyze_data(twitter_data, instagram_data, facebook_data)

if __name__ == "__main__":
    main()