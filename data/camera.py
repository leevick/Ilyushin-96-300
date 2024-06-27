#!/usr/bin/python3
import json
import sys
import time
import requests
from bs4 import BeautifulSoup
import re

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as f:
    lens_data: list[dict] = []

    data = json.load(f)
    total = len(data)
    session = requests.Session()
    for count in range(0, len(data)):
        row = data[count]
        link = row['link']
        fname = link.split('/')[-1]
        photo_id = row['id']
        res = session.get(f"https://russianplanes.net/{photo_id}")
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "lxml")

            camera = soup.find(string=re.compile("Камера"))
            if camera:
                camera = camera.findParent().findChild(name="span").contents[0]
            else:
                camera = ""

            lens = soup.find(string=re.compile("Объектив"))
            if lens:
                lens = lens.findParent().findChild(name="span").contents[0]
            else:
                lens = ""

            focal_length = soup.find(
                name="span", attrs={"title": "фокусное расстояние"})
            if focal_length:
                focal_length = focal_length.contents[0]
            else:
                focal_length = ""

            print(camera, lens, focal_length)

            lens_data.append(
                {"file": fname, "camera": camera, "lens": lens, "focal": focal_length})
        else:
            print(f"lens data failed! status code = {res.status_code}")

        time.sleep(2)
f.close()

with open(output_file, "w") as f:
    json.dump(lens_data, f, ensure_ascii=False, indent=4)
f.close()
