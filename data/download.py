#!/usr/bin/python3
import json
import sys
import time
import requests


with open("photos.json", "r") as f:
    data = json.load(f)
    total = len(data)
    session = requests.Session()
    failed = []
    for count in range(0, len(data)):
        row = data[count]
        link = row['link']
        fname = link.split('/')[-1]
        print(
            f"getting {count}/{total} {round(count * 100 / total,1)}%", flush=True)
        res = session.get(link)
        if res.status_code != 200:
            failed.append(row)
        else:
            with open(fname, "wb") as of:
                of.write(res.content)
            of.close()
        time.sleep(5)

    with open("failed.json", "w", encoding="utf-8") as ff:
        json.dump(failed, ff, ensure_ascii=False)
    ff.close()

f.close()
