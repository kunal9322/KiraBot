import json
import os


def get_user_list(config, key):
    with open("{}/SUMI/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or use this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "16743442"  # integer value, dont use ""
    API_HASH = "12bbd720f4097ba7713c5e40a11dfd2a"
    TOKEN = (
        "5481492613:AAGEoed5DnY2AtZ86nVLaev59Ty8cMa3fB4"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    )
    OWNER_ID = 5885920877  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "MH17_KUNAL"
    SUPPORT_CHAT = "Anime_Krew"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001935950378
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001935950378
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://brmhwhgf:Eq_ZuGoNei_j50ST1iGf7WMymc6IO9vf@hattie.db.elephantsql.com/brmhwhgf"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "YvmbZdX4td1WgKSEun9yG7qVl1WVB9it8hVIyoFEHYFBaTrESPWTIFvyEiF8Esj~"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "PRPSG4AY3Q3H0QG0"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "http://api.timezonedb.com/v2.1/list-time-zone"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    SUMI_STATS_PIC = (
        "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown when you send /stats
    )
    SUMI_WELCOME = "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown when someone adds the bot to group
    SUMI_DIS_WEL = "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown to welcome dragons and dev Disasters when they join a group
    SUMI_OWNER_WEL_IMG = "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown to welcome the owner in the group when he joins
    SUMI_DISPACHER_PIC = (
        "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown when you deploy your bot
    )
    SUMI_HELP_PIC = "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown
    PM_IMAGE = "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown in the pm start when you send /start in bot's pm
    GROUPSTART_VID = "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your video or gif which will be shown when you send /start in groups
    GROUP_ALIVE_PIC = (
        "https://graph.org/file/5ef00f4ce1f0158919522.jpg"  # Paste link of your image which will be shown when you send /alive.
    )
    AFKVID = (
        "https://graph.org/file/0d367a9e7d8d55bd6d41e.mp4"  # Paste link of your video or gif which will be shown when someone goes afk
    )
    NETWORK_NAME = "campusbot"  # Your Network or Community username(without @). IF YOU DONT HAVE ONE, SKIP THIS FIELD
    NETWORK_USERNAME = (
        "Campus_Bot_Updates"  # Your Network or Community name. IF YOU DONT HAVE ONE, SKIP THIS FIELD.
    )
    BOT_USERNAME = "TheVermeil_Bot"  # Your bot username without @.
    BOT_NAME = "vermeil"  # Your bot Name.
    REDIS_URL = ""  # Paste your redis url in format redis://<username of admin role>:<password of admin role>@<endoint url>/<database name>. YOU CAN SKIP THIS IF YOU DONT HAVE ONE
    ARQ_API_KEY = "TLFDRI-BZXGIF-OHRTFM-OIPCWD-ARQ"  # For Some Modules. Get it from @ArqRobot


# Damn, it was tough for me to rewrite this whole, please don't remove the credits from the code, i did too much hardwork for this
# if you face any problem in the bot or its code, please let me know, i will try my best to fix it.
# you can directly pm me(t.me/ishikki_akabane) or you can come in our support group (t.me/suppporttxd)
# thankyou


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
