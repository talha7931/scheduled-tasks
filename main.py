import smtplib
from datetime import datetime as dt
import pandas as pd
import random
import os

# Read the birthdays CSV
data = pd.read_csv("birthdays.csv")

# Get today's date
today = dt.now()
today_tuple = (today.month, today.day)

# Get email credentials from GitHub Secrets (or environment variables)
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# Create a dictionary with (month, day) as the key
birthdays_dict = {
    (row["month"], row["day"]): row
    for (index, row) in data.iterrows()
}

# Check if today is someone's birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # Pick a random letter template
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()

    # Replace the placeholder with the person's name
    content = content.replace("[NAME]", birthday_person["name"])

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )

    print(f"Birthday email sent to {birthday_person['name']}!")

else:
    print("No birthdays today.")
