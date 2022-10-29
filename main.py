print("starting firebot version 1.0")
from pyrogram import Client
from pyrogram.handlers import MessageHandler
import os, string, time, logging, sys, glob, asyncio, traceback
from async_eval import eval
from colorama import init
init()

  
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
