import os
from time import sleep
from pyrogram import Client
import asyncio
from pyrogram import idle


async def main():
    API_ID = "27445409"
    API_HASH = "8fec89a21ba510bf7dc02d3ef6be3279"
    ppk = "BQGiyKEAHr_OfOeBid9ljJn5LEqOZJBrqs5yi4tfHd3bbifihURAMpYc7PrlonwMVlRJL0x0FUjjkAnzGjFGSK5Rvij6yykNN9DlcvDxcc90Lb5iSVPXtSFG0JKI40nuGPznoo6Hl3iL285hmMeXwJhUjI-n_lJw-YW8UydNTIVl7xG5l4XvZlqYZU-vrwSHX9eYXdNfl-PeAFU0k9DSb7zVdgO01JIh9Y3E637jqOJqqn2ffvpyNeG-sWVO2rKJOmtsjdtxgKrbsiwLXoEp6iIvEuWg0pgBwu-adCnmRQIo1y6KwC7A3WTMQT2txkdLbKt2IItJOD-9zzSv2mTvlu8jwBkf1gAAAABfkiJVAA"    
    app = Client(name='userbot', api_id=API_ID, api_hash=API_HASH, session_string=ppk)
    await app.start()
    YAW = await app.export_session_string()
    await app.send_message("me", YAW)
    await idle()
            
            
     
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
