import csv
import os

def get_virtualization_info():
    try:
        # Get the path to the CSV file containing the social media data
        csv_path = os.path.join(os.path.dirname(__file__), 'social_media_data.csv')

        # Read the CSV file
        with open(csv_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            # Initialize dictionaries to store the virtualization information
            virtualization_info = {
                'Twitter': {},
                'Instagram': {},
                'Facebook': {}
            }

            # Iterate over the rows in the CSV file
            for row in reader:
                social_media = row[0]
                handle = row[1]
                followers_count = int(row[2])

                # Check if the handle is already in the virtualization_info dictionary
                if handle in virtualization_info[social_media]:
                    # If the handle is already present, compare the followers count
                    if followers_count > virtualization_info[social_media][handle]:
                        # Update the followers count if it's higher
                        virtualization_info[social_media][handle] = followers_count
                else:
                    # If the handle is not present, add it to the dictionary
                    virtualization_info[social_media][handle] = followers_count

        return virtualization_info

    except FileNotFoundError:
        print("Error: The social_media_data.csv file was not found.")
        return None

    except ValueError:
        print("Error: Invalid data in the social_media_data.csv file.")
        return None

    except Exception as e:
        print("Error:", str(e))
        return None

def write_virtualization_info(virtualization_info):
    try:
        # Get the path to the output file
        output_path = os.path.join(os.path.dirname(__file__), 'virtualization_info.txt')

        # Write the virtualization information to the output file
        with open(output_path, mode='w') as file:
            for social_media, handles in virtualization_info.items():
                file.write(f"{social_media}:\n")
                for handle, followers_count in handles.items():
                    file.write(f"  {handle}: {followers_count}\n")

    except Exception as e:
        print("Error:", str(e))