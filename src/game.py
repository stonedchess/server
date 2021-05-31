from engine.stonedchess.game import Game
from engine.stonedchess.std import fen

from uuid import uuid4


class GameSession:
    """IDfied game store"""

    def __init__(self):
        self.games = dict()

    def __getitem__(self, gid: str) -> Game:
        return self.games[gid]

    def __setitem__(self, gid: str, game: Game):
        self.games[gid] = game

    def std(self) -> str:
        """Create std game"""

        gid = str(uuid4())
        self[gid] = Game(fen())
        return gid
