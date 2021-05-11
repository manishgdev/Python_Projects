import requests
import os.path
from os import path

def checkToken():
    if path.exists("token.txt"):
        print("Token Exists")
    else:
        print("Token file not found")

def generateToken():
    if path.exists("token.txt"):
        print("Token Exists")
        genToken = input("Press Y to use old token, Press N to generate new token")
        if genToken == "Y":
            print("You have selected to generate New Login Token")
        else:
            print("You have selected to proceed with Old Login Token")
    else:
        print("Token file not found")

def main():
    checkToken()

if __name__=="__main__":
    main()