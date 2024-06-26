#!/usr/bin/python3

import json
import pandas as pd

with open("./data/photos.json", encoding="utf-8") as f:
    data = json.load(f)
    df = pd.DataFrame(data)
    numbers = df.groupby('number')
    models = df.groupby('model')

    print(numbers.count().sort_values('id'))
    print(models.count().sort_values('id'))

f.close()
