#!/usr/bin/python

import json

# JSON to DICT
x = '{"name":"Hadi","city":"tehran"}'
y = json.loads(x)


# DICT TO JSON
y = {"name":"Hadi","city":"tehran"}

z = json.dumps(y)

print(z)
