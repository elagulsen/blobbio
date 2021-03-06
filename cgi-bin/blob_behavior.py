#!/usr/bin/env python3

import json
import cgitb
import cgi
import sys
import time
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
INIT_RADIUS = 10
COLORS = ['#a9b6ff' ,  '#ffa9f9', ' #aeffa9',  '#9e76d1' ,  '#ffd983',  '#a4f1de'] # colors used for blobs
BLOT_COLORS = ['#6A5ACD', 'FFD700', '#3CB371', '#BC8F8F', '#CD5C5C']

BLOB_NUMBER = 20
BLOT_NUMBER = 5

cgitb.enable()

data = open("data.json", "w")
update = open("update.json", "r")

player = {"x" : 400, "y": 400, "radius": 25, "colour": "#FFF0F5", "points" : 0}

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
    blob = dict()
    for i in range( number):
        blob[i] = dict()
        blob[i]["x"] = random.randint(0, CANVAS_WIDTH)
        blob[i]["y"] = random.randint(0, CANVAS_HEIGHT)
        blob[i]["colour"] = random.choice(COLORS)
        blob[i]["radius"] = INIT_RADIUS
    return blob
try:
    with open('current_blobs.json') as f:
        blobs = json.load(f)
except:
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
blobs = generate_blots( 20)
all_objects = {"player": player, "blots": blots, "blobs": blobs}

def move( blot):
    time_init = int(round(time.time() * 1000)) #IN MILLISECONDS
    temp = blots.copy()
    temp.append(player)
    
    x1,y1 = blot["x"], blot["y"]
    minv = [-1, -1]
    
    for new_blot in temp:
        if new_blot != blot:
            x2, y2 = new_blot["x"], new_blot["y"],
            dist = ((x2 - x1)**2 + (y2 - y1)**2 )*0.5
            if dist < minv[0] and minv[1] == -1 or blot["radius"] > new_blot["radius"]:
                minv = [dist, new_blot]
    time_cur = -1
    while( time_cur > time_init + 10):
        time_cur = int(round(time.time() * 1000))
    if minv[0] > -1: #if there is a nearby blot or a player 
        d = random.randint(0, 2)
        if d == 1:
            if minv[1]["x"] > blot["x"]:
                blot["x"] += 2
            else:
                blot["x"] -= 2
        else:
            if minv[1]["y"] > blot["y"]:
                blot["y"] += 2
            else:
                blot["y"] -= 2
    return True
    # ELSE go to the nearest blob to gain radius

def collision( blot):
    return False

def blot_update( blot):
    if collision( blot):
        player["points"] += 1
        #eat the blob
    move( blot)

def do(): 
    for blot in blots:
        blot_update( blot)
    data.write(json.dumps(all_objects))
    
do()

data.close()
update.close()