import base64
import ipaddress
import struct
import sys
from telethon.errors.rpcerrorlist import AuthKeyDuplicatedError
from telethon.sessions.string import _STRUCT_PREFORMAT, CURRENT_VERSION, StringSession
import os
from time import sleep

from telethon.errors.rpcerrorlist import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        UserIsBotError,
    )
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


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


_PYRO_FORM = {351: ">B?256sI?", 356: ">B?256sQ?", 362: ">BI?256sQ?"}
DC_IPV4 = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.91",
    5: "91.108.56.130",
}

def encode(ppk):
     ppk = input("Please enter your STRING: ") 
     if len(ppk) in _PYRO_FORM.keys():
         data_ = struct.unpack(
                 _PYRO_FORM[len(ppk)],
                 base64.urlsafe_b64decode(ppk + "=" * (-len(ppk) % 4)),
         )
         if len(ppk) in [351, 356]:
             auth_id = 2
         else:
             auth_id = 3

         dc_id, auth_key = data_[0], data_[auth_id]  
         print(StringSession(
                CURRENT_VERSION
                + base64.urlsafe_b64encode(
                    struct.pack(
                        _STRUCT_PREFORMAT.format(4),
                        dc_id,
                        ipaddress.ip_address(DC_IPV4[dc_id]).packed,
                        443,
                        auth_key,
                    )
                ).decode("ascii")
            ))
         #print(f"BERHASIL YAAA 🙃:\n\n`{CURRENT_VERSION}{stringtele}`\n\n INI DI DECODE LAGI :(\n{data_}")


def encodesstringte():
     ppk = input("Please enter your STRING: ")   
     dk = encode(ppk)
     if len(dk):
         if dk[0] != CURRENT_VERSION:
             raise ValueError("Not a valid string")
         dk = dk[1:]
         ip_len = 4 if len(dk) == 352 else 16
         data_ = struct.unpack(
                _STRUCT_PREFORMAT.format(ip_len), StringSession.decode(dk)
            )

         print(f"=>> Decoded Text :{data_}")
     

def encodes():
     ppk = input("Please enter your STRING: ")     
     if len(ppk):
         if ppk[0] != CURRENT_VERSION:
             raise ValueError("Not a valid string")
         ppk = ppk[1:]
         ip_len = 4 if len(ppk) == 352 else 16
         data_ = struct.unpack(
                _STRUCT_PREFORMAT.format(ip_len), StringSession.decode(ppk)
            )

         print(f"=>> Decoded Text :{data_}")
     


def main():
    print("Waiting")
    try:
        type_of_ss = int(
            input(
                "\nSend decode strings?\n1. Telethon Session.\n2. Pyrogram Session.\n\nEnter choice:  "
            )
        )
    except Exception as e:
        print(e)
        exit(0)
    if type_of_ss == 1:
        encodes()
    elif type_of_ss == 2:
        encode()
    else:
        print("Invalid choice.")
    x = input("Run again? (Y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)

main()
    
