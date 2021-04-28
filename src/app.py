from flask import Flask

import config

app = Flask(__name__)


if __name__ == "__main__":

    app.run(config.HOST, config.PORT, debug=True)