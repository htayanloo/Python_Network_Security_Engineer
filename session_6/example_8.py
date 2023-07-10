#!/usr/bin/python

import requests

response = requests.get("https://dkstatics-public.digikala.com/digikala-products/cd93d6008c517e0fa785725f002f890e06081515_1678613613.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90")

file = open("python.png","wb")

file.write(response.content)

file.close()
