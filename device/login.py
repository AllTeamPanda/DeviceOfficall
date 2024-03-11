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
        API_ID, API_HASH = get_api_id_and_hash()
        ppk = input("Please enter your STRING: ")     
        if len(ppk):
            if ppk[0] != CURRENT_VERSION:
                raise ValueError("Not a valid string")
            ppk = ppk[1:]
            ip_len = 4 if len(ppk) == 352 else 16
            data_ = struct.unpack(
                   _STRUCT_PREFORMAT.format(ip_len), StringSession.decode(ppk)
               )
            auth_id = 2       
            dc_id, auth_key = data_[0], data_[3]       
            test_mode = False
            is_bot = False
            user_id = 1603412565
            api_id = 27445409
            strings = base64.urlsafe_b64encode(
                    struct.pack(
                        SESSION_STRING_FORMAT,
                        dc_id,
                        api_id,
                        test_mode,
                        auth_key,
                        user_id,
                        is_bot
                    )
                ).decode().rstrip("=")   
            app = Client(name='userbot', api_id=API_ID, api_hash=API_HASH, session_string=strings)
            app.start()
            app.send_message("me", f"{strings}")
            idle()
            
            print(f"=>> Decoded Text : Strings Pyrogram:\n\n{strings}")
     
login()
