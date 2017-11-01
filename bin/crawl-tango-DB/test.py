#!/usr/bin/python3

import bs4
import urllib
from bs4 import BeautifulSoup
from pprint import pprint
from data import DBtangoConnexion
import re
#from w3lib.url import safe_url_string




orchestra = 'https://www.el-recodo.com/music?O=Ger%C3%B3nimo+BONGIONI&P=11&lang=fr'

orchestra = re.sub(r'P=\d+','P=2',orchestra)

print (orchestra)











