#!/usr/bin/env python

import requests
import re


target_url = "http://google.com"

def extract_links_form(url):
    response = request(target_url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_link = extract_links_form(target_url)

for link in href_link:
