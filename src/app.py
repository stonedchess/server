from flask import Flask
from flask_cors import CORS as cors

import config
from game import GameSession
from engine import stonedchess as engine

app = Flask(__name__)
store = GameSession()
cors(app)


@app.route("/init")
def init():

    return dict(id=store.std())


@app.route("/<gid>/moves/<int:file>/<int:rank>")
def moves(gid: str, file: int, rank: int):

    game = store[gid]
    position = engine.position.Position(file, rank)
    moves = engine.game.moves(game, position)

    return dict(moves=moves)


@app.route("/<gid>/move/<int:ofile>/<int:orank>/<int:dfile>/<int:drank>")
def move(gid: str, ofile: int, orank: int, dfile: int, drank: int):

    game = store[gid]
    origin = engine.position.Position(ofile, orank)
    destination = engine.position.Position(dfile, drank)
    move = engine.board.Move(origin, destination)
    game.board.move(move)

    winner = game.winner or engine.player.Player.neutral
    return dict(winner=winner.value)


if __name__ == "__main__":

    app.run(config.HOST, config.PORT, debug=True)
