import functions
import os
from modules import whoiis,ddns,cloudflare_bypasser,subdomain,plugins,admin_finder,wpuser,admin_directory_items,site_info,port_scanner,http_header,shell_finder,bug_finder
from pprint import pprint
from sys import platform

try:
    from termcolor import colored, cprint
    from pyfiglet import figlet_format
except:
    os.system("pip install termcolor")
    os.system("pip install requests")
    os.system("pip install pyfiglet")

GREEN = functions.GREEN
RED = functions.RED
BLUE = functions.BLUE
RESET = functions.RESET
WHITE = functions.WHITE

def clear():
    
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')
        
while True :
    clear()
    functions.Tools.banner(None)
    functions.Tools.options(None)

    try:
        
        num = input(f" {RED} [+] {WHITE} Enter a number from the list : {RESET}")
        if num == '1' : ######################### whois
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            whois = whoiis.Information(domain)
            res_Server = whois.Server_info(domain)
            print(f" {RED} \n Result of Server : {GREEN}  ")
            pprint(res_Server)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '2' : ########################## Dns
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            Dns = ddns.Dns_Checker(domain)
            Dns.options()
            num = input(f" {RED} [**] {WHITE} Enter a number from list :  {RESET}")
            if num == '1' :
                res = Dns.A_record(domain)
                print(f" {GREEN} [+] ip ==> {WHITE} {res}")
                print(f" {BLUE} Ended ... {RESET}")
                input()

            elif num == '2' :
                res = Dns.Cname(domain)
                print(f" {GREEN} [+] ip ==> {WHITE} {res}")
                print(f" {BLUE} Ended ... {RESET}")
                input()

            elif num == '3' : 
                res = Dns.Mx_record(domain)
                print(f'{GREEN} Host {res.exchange}  has preference {res.preference} {RESET}') 
                print(f" {BLUE} Ended ... {RESET}")
                input()
            elif num == '00' :
                continue  
        elif num == '3' : ########### bug Finder  
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            bug_finder.bug(domain,GREEN,RED,RESET)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '4' : ############ cloudflare bypasser
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            cloudflare_bypasser.cloudflare(domain)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '5' : ############# Subdomains
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            subdomain.Discover_Subdomains(domain,WHITE,BLUE,RESET,RED,GREEN)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '6' : ############ WordPrss Plugins
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            plugins.Discover_Plugins(domain,BLUE,RESET,RED,GREEN)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '7' : ########### Admin Finder  
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            admin_finder.admin_finder(domain,GREEN,RED,RESET)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '8' : ########### admin directory items  
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            admin_directory_items.items(domain,GREEN,RED,RESET)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '9' : ############ Web Site Info
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            site_info.Fetch_info(domain,GREEN)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '10' : ############ Port scanner
            clear()
            ip = input(f" {RED} [**] {WHITE} Enter a ip :  {RESET}")
            rrange = input(f" {RED} [**] {WHITE} Enter a Range of port :  {RESET}")
            port_scanner = port_scanner.Portscanner(ip,rrange,GREEN,RED,RESET)
            port_scanner.Scan()
            print(f" {BLUE} Ended ... {RESET}")
            input()  
        elif num == '11' : ########### shell Finder  
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            shell_finder.shell(domain,GREEN,RED,RESET)
            print(f" {BLUE} Ended ... {RESET}")
            input()
        elif num == '12' : ############ Http Header
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            res = http_header.http_header(domain)
            print(f"{RED} Results : \n")
            print(f"{WHITE} {res}")
            print(f" {BLUE} Ended ... {RESET}")
            input()   
        elif num == '13' : ############ wordpress username admins
            clear()
            domain = input(f" {RED} [**] {WHITE} Enter a Domain :  {RESET}")
            wpuser.username(domain)
            print(f" {BLUE} Ended ... {RESET}")
            input()
     

        
  

            
    except Exception as e:
        print(f" {RED} Error : {e}")
        input()
        continue
