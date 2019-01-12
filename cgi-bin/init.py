#!/usr/bin/env python3

import json
import cgitb
import cgi
import sys
import time
import random

CANVAS_WIDTH = 8000
CANVAS_HEIGHT = 8000
INIT_RADIUS = 10
COLORS = ['#a9b6ff' ,  '#ffa9f9', ' #aeffa9',  '#9e76d1' ,  '#ffd983',  '#a4f1de'] # colors used for blobs
BLOT_COLORS = ['#6A5ACD', 'FFD700', '#3CB371', '#BC8F8F', '#CD5C5C']

BLOB_NUMBER = 20
BLOT_NUMBER = 5

cgitb.enable()

data = open("data.json", "w")
update = open("update.json", "r")

player = {"x" : 3, "y": 17, "radius": 25, "colour": "#FFF0F5", "points" : 0}

fs = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")
result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"
result['keys'] = ",".join(fs.keys())
d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)
result['data'] = d
sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")
sys.stdout.close()


def generate_blobs( number):
    blobs = []
    for i in range( number+1):
        blob = dict()
        blob["x"] = random.randint(0, CANVAS_WIDTH)
        blob["y"] = random.randint(0, CANVAS_HEIGHT)
        blob["colour"] = random.choice(COLORS)
        blob["radius"] = INIT_RADIUS
        blobs.append(blob)
    return blobs

current_blobs = open("current_blobs.json", "w")
blobs = generate_blobs( BLOB_NUMBER)
current_blobs.write(json.dumps(blobs))

def generate_blots( number):
    blobs = []
    for i in range( number+1):
        blob = dict()
        blob["x"] = random.randint(0, CANVAS_WIDTH)
        blob["y"] = random.randint(0, CANVAS_HEIGHT)
        blob["colour"] = random.choice(BLOT_COLORS)
        blob["radius"] = random.randint(20,30)
        blobs.append(blob)
    return blobs

blots = generate_blots( BLOT_NUMBER)
all_objects = {"player": player, "blots": blots}

data.close()
update.close()
