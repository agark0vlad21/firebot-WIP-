import asyncio, sys
from pyrogram import Client
from pyrogram.handlers import MessageHandler
api_id = 1234567 
api_hash = "0"

app = Client("my_account")


async def sendmessage(chat, text):
    await app.start()
    await app.send_message(chat, text)
    await app.stop()


def send_text_message(chat, text):
    try:
        app.run(sendmessage(chat, text))
        print("sent!")
    except:
        print("not sent:(")


