import json
import time
from firebase_admin import credentials, db, initialize_app

# Load the Firebase service account key
cred = credentials.Certificate('path/to/service_account_key.json')

# Initialize the app with a service account, granting admin privileges
initialize_app(cred, {
    'databaseURL': 'your_firebase_database_url'
})

def calculate_average(data):
    # Define the list of numeric values to calculate average for
    numeric_values = ["cpu_usage", "disk_usage", "load1", "load15", "load5", "monitor_memory", "swap_usage", "temperature"]
    # Initialize dictionaries to store total and count of each numeric value
    total = {key: 0 for key in numeric_values}
    count = {key: 0 for key in numeric_values}
    # Iterate over the data dictionary to calculate total and count for each numeric value
    for key, value in data.items():
        if key in numeric_values:
            total[key] += float(value.strip('% '))
            count[key] += 1
    # Calculate the average for each numeric value
    average = {key: total[key] / count[key] if count[key] > 0 else 0 for key in numeric_values}
    return average

def update_firebase():
    # Open the JSON file and load the data
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    # Get a reference to the root of the Firebase database
    ref = db.reference('/')
    
    # Update the Firebase database with all data from the JSON file
    ref.set(data)
    
    # Calculate average values for numeric data
    average_values = calculate_average(data)

    # Update the Firebase database with the calculated average values
    ref.update(average_values)

# Continuously update Firebase database and calculate average values
while True:
    update_firebase()
    # Wait for 60 seconds before next update
    time.sleep(60)
