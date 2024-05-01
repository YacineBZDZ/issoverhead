import time

import requests
from datetime import datetime
import smtplib
MY_LAT = -40.5334 # Your latitude
MY_LONG = -118.9923 # Your longitude
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your password"
def iss_is_up():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude <= MY_LAT + 5 and iss_latitude >= MY_LAT - 5 and iss_longitude <= MY_LONG + 5 and iss_longitude <= MY_LONG + 5

#Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    # print(time_now.hour, sunset)
    #If the ISS is close to my current position
    # marge_LAT = MY_LAT
while True:
    if  iss_is_up() and is_night():
        # and it is currently dark
        # Then send me an email to tell me to look up.
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr= MY_EMAIL,
                    to_addrs= "jakmca18@gmail.com",
                    msg=f"Subject:look up\n\n The ISS station is over you"
                )
                # BONUS: run the code every 60 seconds.
            time.sleep(60)



