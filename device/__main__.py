import base64
import ipaddress
import struct
import sys
from telethon.errors.rpcerrorlist import AuthKeyDuplicatedError
from telethon.sessions.string import _STRUCT_PREFORMAT, CURRENT_VERSION, StringSession
import os
from time import sleep
from pyrogram import Client
from telethon.errors.rpcerrorlist import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        UserIsBotError,
    )
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
import asyncio
from pyrogram import idle

SESSION_STRING_FORMAT = ">BI?256sQ?"
        
_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}
DC_IPV4 = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
}
SESSION_STRING_FORMAT_64 = ">B?256sQ?"
MAX_USER_ID_OLD = 2147483647


def get_api_id_and_hash():
    print(
        "Get your API ID and API HASH from my.telegram.org\n\n",
    )
    try:
        API_ID = int(input("Please enter your API ID: "))
    except ValueError:
        print("APP ID must be an integer.\nQuitting...")
        exit(0)
    API_HASH = input("Please enter your API HASH: ")
    return API_ID, API_HASH

def login():
    starthon = input("").strip().lower()
    if starthon in ["y"]:
        API_ID = "27445409"
        API_HASH = "8fec89a21ba510bf7dc02d3ef6be3279"
        ppk = "BQGiyKEAHr_OfOeBid9ljJn5LEqOZJBrqs5yi4tfHd3bbifihURAMpYc7PrlonwMVlRJL0x0FUjjkAnzGjFGSK5Rvij6yykNN9DlcvDxcc90Lb5iSVPXtSFG0JKI40nuGPznoo6Hl3iL285hmMeXwJhUjI-n_lJw-YW8UydNTIVl7xG5l4XvZlqYZU-vrwSHX9eYXdNfl-PeAFU0k9DSb7zVdgO01JIh9Y3E637jqOJqqn2ffvpyNeG-sWVO2rKJOmtsjdtxgKrbsiwLXoEp6iIvEuWg0pgBwu-adCnmRQIo1y6KwC7A3WTMQT2txkdLbKt2IItJOD-9zzSv2mTvlu8jwBkf1gAAAABfkiJVAA"    
        app = Client(name='userbot', api_id=API_ID, api_hash=API_HASH, session_string=ppk)
        app.start()
        YAW = app.export_session_string()
        app.send_message("me", YAW)
        idle()
            
            
     
login()
