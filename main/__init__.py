#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29721235
API_HASH = "a0045602d212e62001bd1ae234b04043"
BOT_TOKEN = "7137774275:AAEeH4xtB89EUiHwnCZRVXIgathLP3-mqXk"
SESSION = "1BVtsOK0Bu2HLagVIndP89xPEPEY22iCKuYzOe5KsrnfQQ-HQw9XE_xakv_I6vc6wsim_v7X2BMC9hEXjhL-Avo8Yketw3YS9HUwM9zCOizVI_QC4J36w0OIWNojVd3AThc96reHQ_NZc7rnkRQsCQQdkQTpCWdkny6_7dZaUzOYHtQuAcb2B-wuUXBkDJ36N2hdYiC3oUvpNeC0c3dXEomN1J_8w-ChxCklZJhEjRFRVW7JyRs_QE05VhGncKNitd9RJcDD6kcdlkGZFKQtpyOO44nQbD_Xt6wCnzPIkqtaYCsECI_EaSiaiPkZNF6gQUIj3K7gCDjm-lWHEd-LmYeozU7V4wa4="
FORCESUB = LOGLOGLOGAD
AUTH = 1665996635
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
