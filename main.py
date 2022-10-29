print("starting firebot version 1.0")
from pyrogram import Client
from pyrogram.handlers import MessageHandler
import os, string, time, logging, sys, glob, asyncio, traceback
from async_eval import eval
from colorama import init
init()

if not glob.glob("*.session"):
    print("Not found session file, entering to setup")
    print("Enter api id")
    api_id = int(input())
    print("Enter api hash")
    api_hash = input()

    app = Client("firebot", api_id=api_id, api_hash=api_hash)

    app.run()
    app.stop()

def welcome():
    print(" _____ _          ____        _ ")
    print("|  ___(_)_ __ ___| __ )  ___ | |_")
    print("| |_  | | '__/ _ \  _ \ / _ \| __|")
    print("|  _| | | | |  __/ |_) | (_) | |_")
    print("|_|   |_|_|  \___|____/ \___/ \__|")
    print("importing modules")
    os.chdir("modules")
    for path_to_module in glob.glob("*.py"):
        directory = os.getcwd()
        sys.path.append(directory)
        path = directory + "/" + path_to_module
        module = os.path.basename(os.path.splitext(path)[0])
        try:
            __import__(module)
            print(f"sucessfully imported {module}")
        except:
            print(f"Can't import {module}")

welcome()








#async def main():
#    async with Client("my_account", api_id, api_hash) as app:
#        await app.send_message("me", "Greetings from **Pyrogram**!")

#asyncio.run(main())


