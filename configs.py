import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "21905337"))
  API_HASH = os.environ.get("API_HASH", "581e1c1b5d8213bf30c19d6893c5b2c8")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7578515616:AAFII3G5GOxAcAFz6PpWQ7KwxFxIhUD0KuU")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "GUJJUFILESBOT")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002262936019"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "modijiurl.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "fe930e58ec20ee01ad182f2f4320ff9149c44dc3")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "7802198323"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Sweetgujju:V7JuX2hS1hhdFNq0@cluster0.preom.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002228988489")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002343710976"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 💡FɪʟᴇSᴛᴏʀᴇBᴏᴛ💡]────⍟
│
├🤖 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├📝 Language: [Python 3](https://www.python.org)
│
├🧰 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 🥰 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [👲 LTS](https://t.me/Developerltr_bot)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Developerltr_bot)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
