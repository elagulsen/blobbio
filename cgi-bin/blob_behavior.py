#!/usr/bin/env python3

import json
import cgitb
import cgi
import sys

sys.stdout.write("Content-type: text/html \r\n\r\n")
sys.stdout.write("<!doctype html><html><head><title>Hello CGI</title></head>")
sys.stdout.write("<body><h2>Hello CGI</h2></body></html>")
cgitb.enable()

data = open("data.json", "w")
#update = open("update.json", "r")

player = {"x" : 3, "y": 17, "color": "#FFF0F5", "points" : 0}

blot0= {"x" : 3, "y": 17, "color": "#FFD700"}
blot1= {"x" : 3, "y": 17, "color": "#6A5ACD"}
blot2= {"x" : 3, "y": 17, "color": "#3CB371"}
blot3= {"x" : 3, "y": 17, "color": "#BC8F8F"}
blot4= {"x" : 3, "y": 17, "color": "#CD5C5C"}

blots = [blot0, blot1, blot2, blot3, blot4]

def collision( blot):
    #return true if there is currently a collision
    return True

def blot_update( blot):
    if collision( blot):
        player["points"] += 1
        #eat the blob

while (1):
    for blot_index in range(len(blots)):
        blot_update( blots[blot_index])
        data.write(json.dumps( blots[blot_index]))
    data.write(json.dumps(player))
    break

data.close()
#update.close()
