import socket
import json
import requests

from bs4 import BeautifulSoup

# Config files and variables
config = json.load(open('config.json'))
emoji = json.load(open('emoji.json'))

terraria_ip = config['terraria_ip']
terraria_port = config['terraria_port']

bunhi = emoji['bunhi']
bunsleepy = emoji['bunsleepy']


# Terraria server status
def terraria_status():
    s = socket.socket()
    s.settimeout(5)
    c = s.connect_ex((terraria_ip, terraria_port))
    if c == 0:
        result = 'Server is up ' + bunhi
    else:
        result = 'Server is down ' + bunsleepy
    return result


# Tera server status
def tera():
    page = requests.get('http://tera.enmasse.com/server-status')
    soup = BeautifulSoup(page.content, 'html.parser')
    soupstr = str(soup)
    htmlparse = soupstr.split('\n')
    statusline = htmlparse[179]

    if 'server-up' in statusline:
        return True
    if 'server-down' in statusline:
        return False
