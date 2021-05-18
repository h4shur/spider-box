import os

import requests
try:
    from ipwhois import IPWhois
    import whois
    import socket
    
except:
    os.system("pip install socket.py")
    os.system("pip install python-whois")
    os.system("pip install ipwhois")


class Information:
    def __init__(self,domain) :
        self.domain = domain

    def Get_ip(self,domain):
        ip = socket.gethostbyname(domain)
        return ip
        

    def Server_info(self,domain):
        ip = Information.Get_ip(self=None,domain=domain)
        info = IPWhois(ip)
        info = info.lookup_whois()
        return info    



