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
    IP_ADDRES = {
    1: "149.154.175.53",
    2: "149.154.167.51",
    3: "149.154.175.100",
    4: "149.154.167.40",
    5: "91.108.56.130",
    }
    #IP_ADDRES = int(input("Please enter your IP_ADDRES: "))
    PUBLIC_KEY = input("Please enter your PUBLIC_KEY: ")
    trings = CURRENT_VERSION + base64.urlsafe_b64encode(_STRUCT_PREFORMAT.format(4), 2, ipaddress.ip_address(IP_ADDRES[2]).packed, 443, PUBLIC_KEY,).decode("ascii")
    strings = trings
    print(strings)
    
def main():
    print("Waiting...")
    session()

main()
    
