import pandas as pd
from firebase_admin import credentials, db, initialize_app
import smtplib
from datetime import datetime

# Fetch the service account key JSON file contents
cred = credentials.Certificate('path/to/service_account_key.json')

# Initialize the app with a service account, granting admin privileges
app = initialize_app(cred, {
    'databaseURL': 'your_firebase_database_url'
})

# Get a reference to the database service
ref = db.reference('/')

# Fetch all data
data = ref.get()

# Convert to DataFrame for tabular form display
df = pd.Series(data).to_frame()

# Convert DataFrame to string
df_str = df.to_string()

# Remove the first line of the string
df_str = '\n'.join(df_str.split('\n')[1:])
# print(df_str)

# Setup the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
server.starttls()

# Login to the email account
server.login('your_email@gmail.com', 'your_email_password')

# Create your email
subject = "Linux Monitor System - Data from Firebase"
body = df_str
msg = f"Subject: {subject}\n\n{body}"

# Check if current time is 8:00 PM
current_time = datetime.now().strftime('%H:%M')
if current_time == '20:00':
    # Send an email
    server.sendmail('sender_email@gmail.com', 'recipient_email@gmail.com', msg)
    print("Mail sent")