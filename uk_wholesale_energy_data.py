""" Import functions and libraries required for functionality. """
from timeit import default_timer as timer
import os
import requests
import pandas as pd

# Start Timer.
start = timer()

def main():
    """Main structure calling requested functions from below."""
    print("")
    get_data()

    # End Timer and calculate runtime.
    end = timer()
    total_time = end - start
    print("")
    print(f"This script took approx. {round(total_time, 2)} seconds to complete.")
    print("********************************************************")
    print("")

def get_data():
    """Access Trading Economics chart API and request data shown.
    Remove unwanted values and save final returned result to CSV."""
    try:
        desc = "UK_wholesale_energy_data"
        # Ensure to update the API link with a new authentication key as needed
        api = "https://markets.tradingeconomics.com/chart/gbrelepri:com?span=max&securify=new&url=/united-kingdom/electricity-price&AUTH=KUtMcI%2B%2F%2B7EW7gh0s8u%2BYzSsifHJSBfRRFX8cC7QKRIn5m9SaYkuq7JGsvWjW7nQ7v6eSr0dWH85fCIwGpzBuA%3D%3D&ohlc=0"

        # Access the data API.
        req = requests.get(api, timeout=10)
        response = req.json()

        # Extract the relevant data.
        result = response["series"][0]["data"]
        datafr = pd.DataFrame(result)

        # Ensure the directory exists before saving the file
        os.makedirs("Downloaded_Data", exist_ok=True)

        # Save data to CSV file.
        csv_path = os.path.join("Downloaded_Data", "UK_wholesale_energy_data.csv")
        datafr.to_csv(csv_path, index=False)

        # Confirm action completed.
        print(f"1. Download of {desc} Data was successful.")

    except requests.RequestException:
        print("********************************************************")
        print(f"Request Exception Error, could not download {desc} from API source.")
        print("********************************************************")

    except (KeyError, NameError):
        print("********************************************************")
        print(f"Could not find variable or dictionary value required to save {desc} CSV file.")
        print("********************************************************")

    except Exception:  # pylint: disable=broad-exception-caught
        print("********************************************************")
        print(f"Could not save {desc} CSV file.")
        print("********************************************************")

if __name__ == "__main__":
    main()
