import os
import time
import sys
def bot_start():
    os.system("clear")
    ask = input("Do You Want to Start Bot Spam y/n: ")
    if ask.lower() == "y":
        os.system("python3 -m LegendGirl")
    elif ask.lower() == "n":
        print("\nOk! You Can Start It Later With by using; python3-m LegendGirl\n")
        sys.exit()
    else:
        os.system("clear")
        print("\nInput Must Be y or n")
        bot_start()


def check_again():
    recheck = input(f"\nHave You Filled ALL Vars Correctly?: y/n: ")
    if recheck.lower() == "n":
        os.system("clear")
        print(f"Ohh! Now Fill Your Vars Again")
        LegendStartUP()
    elif recheck.lower() == "y":
        bot_start()
    else:
        print(f"\nInput Must Be Y or N")
        check_again()


def LegendStartUP():
    app_id = input(f"Enter APP_ID: ")
    if app_id:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set APP_ID {app_id}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    api_hash = input(f"\nEnter API_HASH: ")
    if api_hash:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set API_HASH {api_hash}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    HELP_PIC = input(f"\nEnter HELP_PIC (Telegraph link) or press enter!: ")
    if HELP_PIC:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set HELP_PIC {HELP_PIC}")
    PING_PIC = input(f"\nEnter PING_PIC (Telegraph link) or press enter!: ")
    if PING_PIC:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set PING_PIC {PING_PIC}")
    START_PIC = input(f"\nEnter START_PIC (Telegraph link) or press enter!: ")
    if START_PIC:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set START_PIC {START_PIC}")
    START_MESSAGE = input(f"\nEnter START_MESSAGE or press enter!: ")
    if START_MESSAGE:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set START_MESSAGE {START_MESSAGE}")
    LOG_CHANNEL = input(f"\nEnter Chat ID or Username of LOG_CHANNEL or press enter: ")
    if LOG_CHANNEL:
        print("Got it! Fill next value")
        os.system(f"dotenv set LOG_CHANNEL {LOG_CHANNEL}")
    sudo_users = input(f"\nEnter SUDO_USERS (space by space) : ").replace(" ", "\ ")
    if sudo_users:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set SUDO_USERS {sudo_users}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    cmd_hndlr = input(f"\nEnter HANDLER: ")
    if cmd_hndlr:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set HANDLER {cmd_hndlr}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    BOT_TOKEN = input(f"\nEnter session or bot token of BOT TOKEN: ")
    if BOT_TOKEN:
        print(f"Got it! Fill next value")
        os.system(f"dotenv set BOT_TOKEN {BOT_TOKEN}")
    else:
        print(f"You have to fill this variable! all process restarting..")
        time.sleep(2)
        LegendStartUP()
    for i in range(2, 26):
        token = input(f"\nEnter session or bot token of BOT_TOKEN{i} or press enter: ")
        if token:
            print(f"Got it! Fill next value")
            os.system(f"dotenv set BOT_TOKEN{i} {token}")
    check_again()
