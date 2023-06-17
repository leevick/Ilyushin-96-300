from math import ceil
from sys import argv
from PIL import Image

image = Image.open(argv[1])
w, h = image.size
new_image = image.resize((ceil(w / 4) * 4, ceil(h / 4) * 4))
new_image.save(argv[2])
