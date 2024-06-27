#!/usr/bin/python3

import json
import sys

with open(sys.argv[2], encoding="utf-8") as f:
    data = json.load(f)
    for d in data:
        if sys.argv[1] in d["number"]:
            print(d["link"].split("/")[-1])
f.close()
