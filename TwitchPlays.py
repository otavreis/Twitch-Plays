import TwitchPlays_Connection
from TwitchPlays_AccountInfo import TWITCH_USERNAME, TWITCH_OAUTH_TOKEN
import time
import subprocess
import ctypes
import random
import string
import os
from games import *

countdown = 10  #The number of seconds before the code starts running
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

# Connects to your twitch chat, using your username and OAuth token.
# TODO: make sure that your Twitch username and OAuth token are added to the "TwitchPlays_AccountInfo.py" file
t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_USERNAME, TWITCH_OAUTH_TOKEN);

while True:
    # Check for new chat messages
    new_messages = t.twitch_recieve_messages();
    if not new_messages:
        #No new messages. 
        continue
    else:
        try:
            for message in new_messages:
                msg = message['message'].lower()
                username = message['username'].lower()
                #<----GAME HERE----->
                #fallguys(msg)
                marioParty(msg)
        except:
            print('Encountered an exception while reading chat.')
