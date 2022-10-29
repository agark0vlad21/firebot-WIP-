import asyncio, sys
from pyrogram import Client
from pyrogram.handlers import MessageHandler


if not glob.glob("*.session"):
    print("Not found session file, entering to setup")
    print("Enter api id")
    api_id = int(input())
    print("Enter api hash")
    api_hash = input()

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


