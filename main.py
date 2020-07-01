import requests
from bs4 import BeautifulSoup

url = 'chrome://history/'
source_code = requests.get(url)
plain_text = source_code.text
