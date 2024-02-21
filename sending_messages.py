# # noob (me), you need to install pywhatkit first
# # in order to import pywhatkit...

# import pywhatkit
# from datetime import datetime

# PHONE_NUMBER = input("Enter Phone Number: ")
# # Must include all number info about region (and '+' sign).

# MESSAGE = input("Enter Message: ")

# HR = int(input("Enter Hour: "))     
# # 24 Hour Format

# MIN = int(input("Enter Minutes:"))

# pywhatkit.sendwhatmsg(PHONE_NUMBER, MESSAGE, HR, MIN)
# # Send a message at HR:MIN.
# # (Doesn't send until then)
# # (Doesn't close currrent tab, if called again will open another)

# pywhatkit.sendwhatmsg_instantly(PHONE_NUMBER, MESSAGE, tab_close=True)
# # Same, but sends instantly
# # optional args tab_close closes the current tab after sent

# pywhatkit.image_to_ascii_art("folders/name.jpeg", "ascii")
# # tricky, because WhatsApp characters does not align properly


# noob (me), you need to install pywhatkit first
# in order to import pywhatkit...

import pywhatkit
from datetime import datetime, timedelta

PHONE_NUMBER = input("Enter Phone Number: ")

MESSAGE = input("Enter Message: ")

# Setting time delay to 30 seconds
total_seconds = 30

# Calculate the time to send the message
current_time = datetime.now()
send_time = current_time + timedelta(seconds=total_seconds)

# Send the message
pywhatkit.sendwhatmsg(PHONE_NUMBER, MESSAGE, send_time.hour, send_time.minute)

pywhatkit.sendwhatmsg_instantly(PHONE_NUMBER, MESSAGE, tab_close=True)

# Note: image_to_ascii_art() function remains unchanged for ASCII conversion.
