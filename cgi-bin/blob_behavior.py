#!/usr/bin/env python3

import json
import cgitb
import cgi
import sys
import time
import random

sys.stdout.write("Content-type: text/html \r\n\r\n")
sys.stdout.write("<!doctype html><html><head><title>Hello CGI</title></head>")
sys.stdout.write("<body><h2>Hello CGI</h2></body></html>")
cgitb.enable()

data = open("data.json", "w")
update = open("update.json", "r")

player = {"x" : 3, "y": 17, "color": "#FFF0F5", "points" : 0}

blot0= {"x" : 3, "y": 17, "color": "#FFD700"}
blot1= {"x" : 3, "y": 17, "color": "#6A5ACD"}
blot2= {"x" : 3, "y": 17, "color": "#3CB371"}
blot3= {"x" : 3, "y": 17, "color": "#BC8F8F"}
blot4= {"x" : 3, "y": 17, "color": "#CD5C5C"}

blots = [blot0, blot1, blot2, blot3, blot4]
all_objects = {"player": player, "blot0": blot0, "blot1": blot1, "blot2": blot2, "blot3": blot3, "blot4": blot4 }

def collision( blot):
    #return true if there is currently a collision
    return True

def move( blot):
    time_init = int(round(time.time() * 1000)) #IN MILLISECONDS
    
    x1,y1 = blot["x"], blot["y"]
    minv = [-1, -1]
    
    for blot_index in range(len(blots)):
        if blots[blot_index] != blot:
            x2, y2 = blots[ blot_index]["x"], blots[ blot_index]["y"],
            dist = ((x2 - x1)**2 + (y2 - y1)**2 )*0.5
            if dist < minv[0]:
                minv = [dist, blot_index]
    time_cur = -1
    while( time_cur > time_init + 10):
        time_cur = int(round(time.time() * 1000))
    
    d = random.randint(0, 2)
    if d == 1:
        if blots[ minv[1]]["x"] > blot["x"]:
            blot["x"] += 2
        else:
            blot["x"] -= 2
    else:
        if blots[ minv[1]]["y"] > blot["y"]:
            blot["y"] += 2
        else:
            blot["y"] -= 2

def blot_update( blot):
    if collision( blot):
        player["points"] += 1
        #eat the blob
    move( blot)

while (1):
    for blot_index in range(len(blots)):
        blot_update( blots[blot_index])
    data.write(json.dumps(all_objects))
    break

data.close()
update.close()
