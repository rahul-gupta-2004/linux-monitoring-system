# Linux Monitor System

## Description:


* Backend Script (backend.sh):

  * A Bash script that collects system information such as date, time, weather details, memory usage, disk usage, CPU usage, internet connectivity, OS details, network details, and load average.
  * Data is formatted into JSON format and stored in a local file.
  * Continuously runs to update system information in the JSON file.
* Frontend Application (frontend.py):

  * A Python Tkinter GUI application displaying system information retrieved from the JSON file.
  * Utilizes tabs to organize different categories of system information, including basic system and weather information, resource monitoring, network and connectivity details, and system-specific details.
  * Automatically updates information every second for real-time monitoring.
* Firebase Data Storage (firebase_store.py):

  * Retrieves system information from the local JSON file and updates it to a Firebase Realtime Database.
  * Calculates and updates average values for numeric data in the Firebase database.
  * Continuously runs to maintain real-time synchronization between local data and Firebase database.
* Firebase Email Notification (firebase_email.py):

  * Fetches system information from the Firebase Realtime Database.
  * Converts the data into a tabular form using Pandas DataFrame.
  * Sends an email notification containing the system information in tabular format at a specified time (e.g., 8:00 PM).

## Summary of the Steps

* Setup Environment:

  * Ensure you have Bash, Python, and necessary libraries installed.
  * Install required dependencies such as tkinter, PIL, json, firebase_admin, pandas, and smtplib.
* Clone the Repository:

  * Clone the project repository to your local machine using Git.
* Backend Script:

  * Review and customize the backend.sh script as per your requirements.
  * Set the JSON file path and API keys (if required).
  * Execute the script to collect system information and update the JSON file.
* Frontend Application:

  * Understand the structure of the frontend.py Python script.
  * Ensure the data.json file is in the correct directory.
  * Run the frontend application using Python to visualize system information.
* Firebase Integration

  * Obtain a Firebase service account key JSON file and store it in the appropriate directory.
  * Review and modify the firebase_store.py and firebase_email.py scripts as per your Firebase project configuration.
  * Run firebase_store.py to update system information in the Firebase Realtime Database.
  * Customize firebase_email.py to set the email notification schedule and recipient.
* Contribution Guidelines:

  * Fork the repository if you intend to contribute.
  * Create a new branch for your changes.
  * Make modifications or additions to the scripts as needed.
  * Test your changes thoroughly.
  * Submit a pull request with a detailed description of your changes.
* Feedback and Support:

  * Provide feedback or report any issues encountered during usage.
* Reach out to the project maintainers for support or clarification on any aspect of the project.

## Built With

* Bash Scripting:

  * Used for the backend script (backend.sh) to collect system information.
* Python:

  * Utilized for the frontend application (frontend.py) to create the graphical user interface (GUI) using Tkinter.
  * Used for data manipulation and analysis in scripts like firebase_store.py and firebase_email.py.
* Python Libraries:

  * Tkinter: Python library for creating GUI applications.
  * PIL (Python Imaging Library): Python library for image processing.
  * JSON: Python library for handling JSON data.
  * Firebase Admin SDK: Python library for integrating Firebase services.
  * Pandas: Python library for data manipulation and analysis.
  * smtplib: Python library for sending emails.
* Data Storage:

  * Firebase Realtime Database: Used for storing and synchronizing system data in real-time.
* Other Tools:

  * curl: Command-line tool for transferring data with URLs (used for API requests in backend.sh).
  * jq: Command-line JSON processor (used for parsing JSON responses in backend.sh).
* Integrated Development Environment (IDE):

  * Visual Studio Code (VS Code): A popular code editor used for writing, debugging, and managing the project's source code.
* Operating System:

  * Linux (Pop!_OS): Specifically, Pop!_OS, a Linux distribution based on Ubuntu, was used as the development environment for creating and testing the system monitoring project.

## Features

* System Monitoring:

  * Continuously monitors various system metrics including CPU usage, memory usage, disk usage, swap usage, and load average.
* Real-time Weather Information:

  * Retrieves and displays real-time weather information such as temperature and weather description for a specified city.
* Graphical User Interface (GUI):

  * Provides a user-friendly interface implemented using Tkinter, allowing users to easily view system and weather data.
* Internet Connectivity Status:

  * Indicates whether the system is connected to the internet and displays the name of the connected Wi-Fi network (if applicable).
* Operating System Details:

  * Retrieves and presents details about the device's operating system, including OS type, name, version, architecture, and kernel release.
* Network Information:

  * Shows internal and external IP addresses, along with DNS server details.
* Firebase Integration:

  * Automatically updates a Firebase Realtime Database with system data, enabling remote monitoring and analysis.
* Email Notification:

  * Sends email notifications containing system data at a specified time (e.g., daily report).

## System Flowchart

The flowchart below illustrates the flow of data and operations within the system.

![System Flowchart](https://i.postimg.cc/85RDNdQv/flowchart.png)

## Usage/Examples

### Running the Project:

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/your-project.git
```

2. Navigate to the project directory:

```
cd your-project
```

3. Ensure you have all the required dependencies installed. If not, install them using pip:

* Install Tkinter

```
    pip install tkinter
```

* Install Pillow (Python Imaging Library)

```
    pip install Pillow
```

* Install Firebase Admin SDK

```
    pip install firebase-admin
```

* Install Pandas

```
    pip install pandas
```

* Install Requests

```
    pip install requrests
```

* Install smptlib

```
    pip install smtplib
```

4. Run the backend script to start collecting system information:

```
bash backend.sh
```

5. Open another terminal window and run the frontend application to visualize system information:

```
python frontend.py
```

6. Explore the GUI interface to view various system metrics and real-time weather information.
7. Run the program automatically when the device starts by executing the following commands in the Bash console

```
nohup backend.sh &
nohup python3 firebase_store.py &
nohup python3 firebase_email.py &
```

8. Note down or remember these commands as they will be used to set up startup programs.
9. Open "Startup Applications" in Linux Pop!_OS:

* Navigate to the applications menu and search for "Startup Applications."
* Click on "Startup Applications" to open the settings.

10. Click on "Add" to add a new startup program.
11. Enter the following details:

* Name: Provide a descriptive name for the startup program.
* Command: Enter the command corresponding to each script:

  ```
    nohup backend.sh &
  ```

  ```
    nohup python3 firebase_store.py &
  ```

  ```
    nohup python3 firebase_email.py &
  ```
* Comment: Optionally, add a brief comment to describe the startup program.

12. After adding the startup programs, restart your system to apply the changes.
13. After restarting, verify if the files are being executed using the following commands:

```
  ps aux | grep backend.sh
```

```
  ps aux | grep python
```

These commands will display any processes related to the backend script and Python scripts respectively.

### Screenshots:

Initial screen displaying the project logo and title.

![A splash screen displaying the project logo and title.](https://i.postimg.cc/dhCTfcry/1.png)

Graphical user interface divided into multiple panes showing real-time system metrics, weather information, network details, and system-specific data.

![Pane 1 showing real-time system metrics such as CPU and memory usage.](https://i.postimg.cc/GTpygBxL/2.png)

![Pane 2 displaying weather information including temperature and weather description.](https://i.postimg.cc/tYwxD4Zb/3.png)

![Pane 3 presenting network details such as internal and external IP addresses.](https://i.postimg.cc/3ddGgvw9/4.png)

![Pane 4 showcasing system-specific details like operating system type and kernel release.](https://i.postimg.cc/5jPvY3f6/5.png)

Sample email notification containing system data in tabular format.

![An image displaying a sample email notification containing system data in tabular format.](https://i.postimg.cc/5Ygzm5vK/6.png)

### Code Snippets:

Collecting System Information (backend.sh):

```
#!/bin/bash

# Collect system information
date=$(date +"%Y-%m-%d")
time=$(date +"%T")
weather=$(curl -s "https://api.openweathermap.org/data/2.5/weather?q=city&appid=your_api_key")
# Add more commands to collect additional information

# Format data into JSON
json_data=$(cat <<EOF
{
  "date": "$date",
  "time": "$time",
  "weather": "$weather",
  # Add more fields as necessary
}
EOF
)

# Store data in JSON file
echo "$json_data" > data.json

```

Displaying System Information (frontend.py):

```
import tkinter as tk

# Create GUI window
window = tk.Tk()
window.title("System Monitor")

# Add widgets to display system information
label = tk.Label(window, text="System Metrics")
label.pack()

# Add more widgets to display additional information

# Run GUI application
window.mainloop()

```

### Use Cases:

* Monitoring system performance in real-time.
* Analyzing resource usage trends over time.
* Checking weather information alongside system metrics for better context.
* Generating daily reports for system administrators.

### Tips:

* Customize the frontend GUI layout and styling to suit your preferences.
* Explore additional APIs or data sources to enhance the project's functionality further.

## API Reference

### OpenWeatherMap API

#### Get Weather Information

```http
GET https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}
```

| Parameter   | Type       | Description                          |
| :---------- | :--------- | :----------------------------------- |
| `city`    | `string` | **Required**. Name of the city |
| `api_key` | `string` | **Required**. Your API key     |

### Firebase Realtime Database API

#### Update System Data

```http
  GET https://your-project-id.firebaseio.com/data.json
```

| Parameter | Type     | Description                                   |
| :-------- | :------- | :-------------------------------------------- |
| `data`  | `json` | **Required**. System data to be updated |
