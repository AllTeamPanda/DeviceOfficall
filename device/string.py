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
import os
import struct
from hashlib import sha1
try:
    import rsa
    import rsa.core
except ImportError:
    rsa = None
    raise ImportError('Missing module "rsa", please install via pip.')

from telethon.tl import TLObject


# {fingerprint: (Crypto.PublicKey.RSA._RSAobj, old)} dictionary
_server_keys = {}



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
     
def get_byte_array(integer):
    """Return the variable length bytes corresponding to the given int"""
    # Operate in big endian (unlike most of Telegram API) since:
    # > "...pq is a representation of a natural number
    #    (in binary *big endian* format)..."
    # > "...current value of dh_prime equals
    #    (in *big-endian* byte order)..."
    # Reference: https://core.telegram.org/mtproto/auth_key
    return int.to_bytes(
        integer,
        (integer.bit_length() + 8 - 1) // 8,  # 8 bits per byte,
        byteorder='big',
        signed=False
    )


def _compute_fingerprint(key):
    """
    Given a RSA key, computes its fingerprint like Telegram does.

    :param key: the Crypto.RSA key.
    :return: its 8-bytes-long fingerprint.
    """
    n = TLObject.serialize_bytes(get_byte_array(key.n))
    e = TLObject.serialize_bytes(get_byte_array(key.e))
    # Telegram uses the last 8 bytes as the fingerprint
    return struct.unpack('<q', sha1(n + e).digest()[-8:])[0]


def add_key(pub, *, old):
    """Adds a new public key to be used when encrypting new data is needed"""
    global _server_keys
    key = rsa.PublicKey.load_pkcs1(pub)
    _server_keys[_compute_fingerprint(key)] = (key, old)


def encrypt(fingerprint, data, *, use_old=False):
    """
    Encrypts the given data known the fingerprint to be used
    in the way Telegram requires us to do so (sha1(data) + data + padding)

    :param fingerprint: the fingerprint of the RSA key.
    :param data: the data to be encrypted.
    :param use_old: whether old keys should be used.
    :return:
        the cipher text, or None if no key matching this fingerprint is found.
    """
    global _server_keys
    key, old = _server_keys.get(fingerprint, [None, None])
    if (not key) or (old and not use_old):
        return None

    # len(sha1.digest) is always 20, so we're left with 255 - 20 - x padding
    to_encrypt = sha1(data).digest() + data + os.urandom(235 - len(data))

    # rsa module rsa.encrypt adds 11 bits for padding which we don't want
    # rsa module uses rsa.transform.bytes2int(to_encrypt), easier way:
    payload = int.from_bytes(to_encrypt, 'big')
    encrypted = rsa.core.encrypt_int(payload, key.e, key.n)
    # rsa module uses transform.int2bytes(encrypted, keylength), easier:
    block = encrypted.to_bytes(256, 'big')
    return block


for pub in (
        '''-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAvmpxVY7ld/8DAjz6F6q05shjg8/4p6047bn6/m8yPy1RBsvIyvuD
uGnP/RzPEhzXQ9UJ5Ynmh2XJZgHoE9xbnfxL5BXHplJhMtADXKM9bWB11PU1Eioc
3+AXBB8QiNFBn2XI5UkO5hPhbb9mJpjA9Uhw8EdfqJP8QetVsI/xrCEbwEXe0xvi
fRLJbY08/Gp66KpQvy7g8w7VB8wlgePexW3pT13Ap6vuC+mQuJPyiHvSxjEKHgqe
Pji9NP3tJUFQjcECqcm0yV7/2d0t/pbCm+ZH1sadZspQCEPPrtbkQBlvHb4OLiIW
PGHKSMeRFvp3IWcmdJqXahxLCUS1Eh6MAQIDAQAB
-----END RSA PUBLIC KEY-----''',

):
    add_key(pub, old=False)
        
def rsa():
     pub = input("Please enter your Api Key public: ")     
     aunthkey = rsa.PublicKey.load_pkcs1(pub)
     print(aunthkey)

def main():
    print("Waiting")
    try:
        type_of_ss = int(
            input(
                "\nSend decode strings?\n1. Telethon Session.\n2. Pyrogram Session\n3 Telethon decode.\n5.Rsa.\n\nEnter choice:  "
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
    elif type_of_ss == 5:
        rsa()
    else:
        print("Invalid choice.")
    x = input("Run again? (Y/n)")
    if x.lower() in ["y", "yes"]:
        main()
    else:
        exit(0)

main()
    
