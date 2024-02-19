""" Import functions and libraries required for functionality. """
from timeit import default_timer as timer
import os
import requests
import pandas as pd

# Start Timer.
start = timer()

def main():
    """Main structure calling requested functions."""
    start = timer()  # Start the timer

    api = read_api_url()  # Read API URL from file
    if api:
        get_data(api)

    # End Timer and calculate runtime.
    end = timer()
    total_time = end - start
    print(f"\nThis script took approx. {round(total_time, 2)} seconds to complete.")
    print("********************************************************\n")

def read_api_url():
    """Read the API URL from a file."""
    try:
        with open("API.txt", "r") as file:
            return file.readline().strip()  # Read the first line with strip to remove newline characters
    except FileNotFoundError:
        print("API.txt file not found. Please ensure the file exists in the same directory as this script.")
        exit()

def get_data(api):
    """Access API and request data shown. Remove unwanted values and save the result to CSV."""
    desc = "UK_wholesale_energy_data"
    try:
        # Access the data API.
        req = requests.get(api, timeout=10)
        req.raise_for_status()  # Raises a HTTPError if the response status code is 4XX/5XX
        response = req.json()

        # Extract the relevant data.
        result = response["series"][0]["data"]
        datafr = pd.DataFrame(result)

        # Ensure the directory exists before saving the file
        os.makedirs("Downloaded_Data", exist_ok=True)

        # Save data to CSV file.
        csv_path = os.path.join("Downloaded_Data", f"{desc}.csv")
        datafr.to_csv(csv_path, index=False)

        # Confirm action completed.
        print(f"1. Download of {desc} Data was successful.")

    except requests.HTTPError as http_err:
        print("********************************************************")
        print(f"HTTP Error occurred: {http_err}")
        print("********************************************************")
    except requests.RequestException as req_err:
        print("********************************************************")
        print(f"Request Exception Error, could not download {desc} from API source: {req_err}")
        print("********************************************************")
    except Exception as e:  # Catching other exceptions
        print("********************************************************")
        print(f"An unexpected error occurred: {e}")
        print("********************************************************")

if __name__ == "__main__":
    main()
