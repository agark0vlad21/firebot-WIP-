import sys, os, glob
from pyrogram import Client
from pyrogram.handlers import MessageHandler




if not glob.glob("*.session"):
    print("Not found session file, entering to setup")
    print("Enter api id")
    api_id = int(input())
    print("Enter api hash")
    api_hash = input()


def send_message(chat, message):
    with Client(session, api_id, api_hash) as app:
        app.send_message(chat, message)

def send_photo(chat, photo):
    with Client(session, api_id, api_hash) as app:
        app.send_photo(chat, photo)

def send_photo(chat, photo):
    with Client(session, api_id, api_hash) as app:
        app.send_photo(chat, photo)

def send_document(chat, document):
    with Client(session, api_id, api_hash) as app:
        app.send_document(chat, document)


@app.on_message()
def my_handler(client, message):
    print(message)
    exit()

def run_handler():
    app.run()

