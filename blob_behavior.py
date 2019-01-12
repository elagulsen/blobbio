import json

data = open("data.json", "w")

player = {"x" : 3, "y": 17, "color": "#FFF0F5", "points" : 0}

blot0= {"x" : 3, "y": 17, "color": "#FFD700"}
blot1= {"x" : 3, "y": 17, "color": "#6A5ACD"}
blot2= {"x" : 3, "y": 17, "color": "#3CB371"}
blot3= {"x" : 3, "y": 17, "color": "#BC8F8F"}
blot4= {"x" : 3, "y": 17, "color": "#CD5C5C"}

if_collision():
    #return true if there is currently a collision
    return True

blot_update():
    if_collision():
        #eat the blob
        print("yeet")

while (1):
    data.write(json.dumps(player))
    data.write(json.dumps(blot0))
    data.write(json.dumps(blot1))
    data.write(json.dumps(blot2))
    data.write(json.dumps(blot3))
    data.write(json.dumps(blot4))

data.close()
