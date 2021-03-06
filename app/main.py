import bottle
import os
import random

from board_frame import BoardFrame
from snake_util import *

height = 0
width = 0
name = 'crazysnake5'

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
    global name

    return {
        "taunt": "ohno",
        "name": name,
        "color": "#689d22",
        "head_url": head_url
    }


@bottle.post("/move")
def move():

    data = bottle.request.json
    global name

    height = len(data['board'])

    width = len(data['board'][0])

    board = BoardFrame(data, height, width, name)
    
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
            "move": "up",
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


