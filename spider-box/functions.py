import os
try:
    from colorama import init,Fore
    from termcolor import colored, cprint
    from pyfiglet import figlet_format
except:
    os.system("pip install termcolor")
    os.system("pip install colorama")
    os.system("pip install pyfiglet")
    

init() # Call Colors
GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
RESET = Fore.RESET
WHITE = Fore.WHITE

class Tools:

    def banner(self=None):
        print(f""" {Fore.CYAN}
        

{figlet_format("spider box")}
                  {Fore.CYAN}                                                 
###############################################################
#                      Developer : h4shur                     #
#      Telegram & Instagram & Twitter & Github : @h4shur      #
#                      h4shursec@gmail.com                    #
###############################################################                               
        {RESET}""")
        
    def options(self=None):
            print(f"""
        OPTIONS :
        {GREEN}
        [ 1 ]   -  Server Whois
        [ 2 ]   -  Dns Checker
        [ 3 ]   -  bug finder (321 page)
        [ 4 ]   -  cloudflare bypass
        [ 5 ]   -  Sub Domains (19656 sub domain)
        [ 6 ]   -  WordPress Plugins (297 plugin)
        [ 7 ]   -  Admin Page Finder (8185 page)
        [ 8 ]   -  admin directory & page items (134 item)
        [ 9 ]   -  WebSite Information
        [ 10 ]  -  Port Scanner
        [ 11 ]  -  shell Finder (154 page)
        [ 12 ]  -  Show HTTP Header
        [ 13 ]  -  Wordpress username admins
        
        {RESET}
        """)
    
