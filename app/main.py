import bottle
import os
import random

from board_frame import BoardFrame
from snake_util import *

height = 0
width = 0

@bottle.route("/static/<path:path>")
def static(path):
    return bottle.static_file(path, root="static/")


@bottle.get("/")
def index():
    head_url = "%s://%s/static/head.png" % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        "color": "#689D22",
        "head": head_url
    }


@bottle.post("/start")
def start():
    data = bottle.request.json

    head_url = "%s://%s/static/head.png" % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    global height
    height = data["height"]
    global width
    width = data["width"]

    return {
        "taunt": "ohno"
    }


@bottle.post("/move")
def move():

    data = bottle.request.json
    global height
    global width
    board = BoardFrame(data, height, width)
    
    if board.foods:
        dest = closestFood(board)
    else:
        if (board.ourLoc == [board.width-1,board.height-1]):
            dest = [0,0]
        else:
            dest = [board.width-1,board.height-1]

    move = findMove(board, dest)

    if not idealMove(board, move):
        move = altMove(board, move, dest)

    print "move: " + move
    # Return move
    if move == "no_safe":
        print "ERROR!"
        return{
            "move": "north",
            "taunt": "ERROR!"
        }

    else:
        return {
            "move": move,
            "taunt": ":0"
        }


@bottle.post("/end")
def end():
    data = bottle.request.json


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == "__main__":
    bottle.run(application, host=os.getenv("IP", "0.0.0.0"), port=os.getenv("PORT", "8080"))


