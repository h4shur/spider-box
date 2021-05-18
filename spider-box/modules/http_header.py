
import os

try:
    import requests
except:
    os.system("pip install requests")

def http_header(domain) :

    response = requests.get('http://'+domain)
    return response.headers
