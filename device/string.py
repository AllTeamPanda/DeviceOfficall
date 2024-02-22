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

    IP_ADDRES = input("Please enter your IP_ADDRES: ")
    
    PUBLIC_KEY = input("Please enter your PUBLIC_KEY: ")
    ip = ipaddress.ip_address(IP_ADDRES).packed
    trings = CURRENT_VERSION + StringSession.encode(struct.pack(_STRUCT_PREFORMAT.format(len(ip)), 2, ip, 443, PUBLIC_KEY,))
    print(trings)
    
def main():
    print("Waiting...")
    session()

main()
    
