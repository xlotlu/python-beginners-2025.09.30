import os
from os import path
from os.path import join

BASE_DIR = '/tmp/work-folder'

print(
    join(BASE_DIR, "subfolder", "etc", "myfile.txt")
)


# exercițiu
# faceți import unui modul dintre
# os, datetime.date, datetime.datetime, csv, json, math, random