

import os

try:
    import requests
except:
    os.system("pip install requests")
    

def username(domain):
    r = requests.get('http://'+domain+'/wp-json/wp/v2/users/')

    print (r.json())

