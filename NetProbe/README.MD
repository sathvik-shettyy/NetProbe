A project by Sathvik D Shetty
This project (Netprobe) is a social media data collector that fetches data from Twitter, Instagram, and Facebook APIs, stores the data, analyzes it, and provides virtualization information based on the collected data.

## Features

- Fetch data from Twitter, Instagram, and Facebook APIs
- Store the collected data in a database
- Write the data to a CSV file for easy access
- Analyze the collected data
- Provide virtualization information based on followers count

## Installation

1. Clone the repository
2. Install the required packages by running:
   ```bash
   pip install -r requirements.txt
Usage
Set up API keys for Twitter, Instagram, and Facebook in the respective client files
Run the main script to collect data: python main.py
The collected data will be stored in the database, CSV file, and analyzed accordingly

## Project Structure
twitter_client.py: Contains functions to interact with the Twitter API
instagram_client.py: Contains functions to interact with the Instagram API
facebook_client.py: Contains functions to interact with the Facebook API
database.py: Functions to store data in a database
csv_handler.py: Functions to write data to a CSV file
data_analyzer.py: Functions to analyze the collected data
virtualization.py: Functions to provide virtualization information


## License
This project is licensed under the MIT License - see the LICENSE file for details.
