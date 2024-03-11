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
def clear_screen():
    # https://www.tutorialspoint.com/how-to-clear-screen-in-python#:~:text=In%20Python%20sometimes%20we%20have,screen%20by%20pressing%20Control%20%2B%20l%20.
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")
            
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
        

def get_pyro():
    print(
        "String sessions terbaru \n\n",
    )
    API_ID, API_HASH = get_api_id_and_hash()
    SESSION = input("Please enter your SESSIONS: ")
    app = Client('userbot', api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
    app.start()
    
    

def get_ipaddres():
    print(
        "Get your IP_ADDRES and PUBLIC_KEY from my.telegram.org.\n\n",
    )
    try:
        IP_ADDRES = input("Please enter your IP_ADDRES: ")
    except ValueError:
        print("IP_ADDRES must be an integer.\nQuitting...")
        exit(0)
    PUBLIC_KEY = input("Please enter your PUBLIC_KEY: ")
    return IP_ADDRES, PUBLIC_KEY

def session():

    IP_ADDRES = input("Please enter your IP_ADDRES: ")
    
    PUBLIC_KEY = input("Please enter your PUBLIC_KEY: ")
    ip = ipaddress.ip_address(IP_ADDRES).packed
    trings = CURRENT_VERSION + StringSession.encode(struct.pack(_STRUCT_PREFORMAT.format(len(ip)), 2, ip, 443, PUBLIC_KEY,))
    print(trings)

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

def encode():
     ppk = input("Please enter your STRING: ") 
     if len(ppk) in _PYRO_FORM.keys():
         data_pyro = struct.unpack(
                 _PYRO_FORM[len(ppk)],
                 base64.urlsafe_b64decode(ppk + "=" * (-len(ppk) % 4)),
         )
         if len(ppk) in [351, 356]:
             auth_id = 2
         else:
             auth_id = 3

         dc_id, auth_key = data_pyro[0], data_pyro[auth_id]  
         encodestring = CURRENT_VERSION + base64.urlsafe_b64encode(struct.pack(_STRUCT_PREFORMAT.format(4), dc_id, ipaddress.ip_address(DC_IPV4[dc_id]).packed, 443, auth_key,)).decode("ascii")
         if len(encodestring):
             if encodestring[0] != CURRENT_VERSION:
                 raise ValueError("Not a valid string")
             encodestring = encodestring[1:]
             ip_len = 4 if len(encodestring) == 352 else 16
             data_ = struct.unpack(
                    _STRUCT_PREFORMAT.format(ip_len), StringSession.decode(encodestring)
                )   
         print(f"BERHASIL YAAA 🙃:\n\n`{encodestring}`\n\n INI DI DECODE LAGI :(\nTelethon:\n{data_}\nDC :{data_[0]}\n{data_[auth_id]}\n\nPyrogram:\n{data_pyro}")


def encodesstringte():
     ppk = input("Please enter your STRING: ")   
     dk = ppk
     if len(dk):
         if dk[0] != CURRENT_VERSION:
             raise ValueError("Not a valid string")
         dk = dk[1:]
         ip_len = 4 if len(dk) == 352 else 16
         data_ = struct.unpack(
                _STRUCT_PREFORMAT.format(ip_len), StringSession.decode(dk)
            )

         print(f"=>> Decoded Text :NOL:{data_[0]}\n\n1:{data_[1]}\n\n2: {data_[2]}\n\n3: {data_[3]}")
     

def encodes():
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
         
          print(f"=>> Decoded Text : Strings Pyrogram:\n\n{strings}\n\nDECODE TELETHON🙃:\n{data_}")
     


def main():
    print("Waiting")
    try:
        type_of_ss = int(
            input(
                "\nSend decode strings?\n1. Telethon Session.\n2. Pyrogram Session\n3 Telur dadar.\n\nEnter choice:  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        encodes()
    elif type_of_ss == 2:
        encode()
    elif type_of_ss == 3:
        encodesstringte()
    elif type_of_ss == 4:
        get_pyro()
    else:
        print("Invalid choice.")
    x = input("Run again? (Y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)

main()
    
