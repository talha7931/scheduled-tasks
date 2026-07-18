import smtplib
from datetime import datetime as dt
import pandas as pd
import random


# 2. Check if today matches a birthday in the birthdays.csv
file=pd.read_csv("birthdays.csv")
today = dt.now()
today_day = today.day
today_month = today.month
today_tuple = (today_day, today_month)

data=pd.read_csv("birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    bithday_person=birthdays_dict[today_tuple]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content=letter_file.read()
        content.replace("[Name]",bithday_person["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login("smohammadtalha0@gmail.com","umya zowy avqj fnwv")
        connection.sendmail(
            to_addrs=bithday_person["email"],
            from_addr="smohammadtalha0@gmail.com",
            msg=f"Happy birthday {file_path}"
        )




