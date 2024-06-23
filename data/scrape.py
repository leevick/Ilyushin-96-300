#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from time import sleep
import json
import sys

def parse_list(text: str) -> list[dict[str, str | int]]:
    res: list[str] = []
    soup = BeautifulSoup(text, "lxml")
    divs = soup.find_all("div", class_="photographer__avimedia__photo")
    if len(divs) == 0:
        return res
    for div in divs:
        a = div.findChild('a', recursive=False)
        im = a.findChild('img', recursive=True)
        info = div.findChild('div', class_='photographer__avimedia__info')
        p = info.findChild('p', recursive=True)
        aircraft_type = p.contents[0].strip().replace("Тип: ", "")
        aircraft_model = p.contents[2].strip().replace("Мод.: ", "")
        aircraft_number = p.contents[4].strip().replace("Бортовой: ", "")
        res.append({"id": a['href'].replace("/", ""), "link": im['src'].replace("-525.", "."), "type": aircraft_type,
                   "model": aircraft_model, "number": aircraft_number})
    return res


def get_photo_list(session: requests.Session, url: str) -> list[dict[str, str | int]]:
    lst: list[dict[str, str | int]] = []
    idx: int = 1
    while True:
        print("getting photo lists %d\n", idx)
        res = session.post("https://russianplanes.net"+url,
                           data={"page": idx, "setyp": "3||56", "ajax": "1"})
        sublst = parse_list(res.text)
        if (len(sublst) == 0):
            break
        lst.extend(sublst)
        idx = idx + 1
        sleep(1)
    return lst


session = requests.Session()


session.get("https://russianplanes.net")
res = session.post("https://russianplanes.net/search", data={"sereq": "",
                                                             "setyp":	"3||56",
                                                             "secat":	"",
                                                             "sesubcat":	"",
                                                             "seal":	"",
                                                             "seport":	"",
                                                             "category":	"",
                                                             "sort":	"",
                                                             "thereAreInReg":	"",
                                                             "video":	"",
                                                             "hidden":	"",
                                                             "sereg":	"",
                                                             "secn":	"",
                                                             "cratko":	"on", })

soup = BeautifulSoup(res.text, "lxml")
url = soup.find("div", id="pageUrlLink1").contents[0]
photos = get_photo_list(session, url)

with open(sys.argv[1], "w", encoding="utf-8") as f:
    json.dump(photos, f, ensure_ascii=False, indent=4)
    f.close()
