# Complete Snippet to send message to a number at 15:00
# ----------------------------------------

import pywhatkit 
try: 
	pywhatkit.sendwhatmsg("+91**********", "Welcome to contribute with hacktober", 15, 00)
	print("Message Sent Successfully!") 

except: 
	print("Unexpected Error Occured while sending message")

#----------------------------------------
# Output on running sippet
# Message Sent Successfully!
