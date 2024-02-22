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
        IP_ADDRES = int(input("Please enter your IP_ADDRES: "))
    except ValueError:
        print("IP_ADDRES must be an integer.\nQuitting...")
        exit(0)
    PUBLIC_KEY = input("Please enter your PUBLIC_KEY: ")
    return IP_ADDRES, PUBLIC_KEY

def session():
    try:
        IP_ADDRES, PUBLIC_KEY = get_ipaddres()
        API_ID, API_HASH = get_api_id_and_hash()
    except ImportError:
        print("Eror..")
    return strings = StringSession(
        CURRENT_VERSION
        + base64.urlsafe_b64encode(
            struct.pack(
                _STRUCT_PREFORMAT.format(4),
                dc_id,
                ipaddress.ip_address(IP_ADDRES).packed,
                443,
                PUBLIC_KEY,
            )
        ).decode("ascii")
    )
    print(f"{strings}")  
    try:
        with TelegramClient(strings, API_ID, API_HASH) as bot:
            print("Generating a string session for •Userbot•")
            try:
                bot.send_message(
                    "me",
                    f"**Userbot** `SESSION`:\n\n`{bot.session.save()}`\n\n**Do not share this anywhere!**",
                )
                print(
                    "Your SESSION has been generated. Check your Telegram saved messages!"
                )
                return
            except UserIsBotError:
                print("You are trying to Generate Session for your Bot's Account?")
                print("Here is That!\n{ultroid.session.save()}\n\n")
                print("NOTE: You can't use that as User Session..")
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nQuitting..."
        )
        exit(0)
    except ValueError:
        print("API HASH must not be empty!\nQuitting...")
        exit(0)
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nQuitting...")
        exit(0)
    except Exception as er:
        print("Unexpected Error Occurred while Creating Session")
        print(er)
        print("If you think It as a Bug, Report to @UltroidSupportChat.\n\n")

def main():
    print("Waiting...")
    session()

main()
    
