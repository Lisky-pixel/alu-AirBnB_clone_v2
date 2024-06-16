#!/usr/bin/python3
"""Start a flask web app
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
<<<<<<< HEAD
=======
    app.url_map.strict_slashes = False
>>>>>>> e21d8ebbde54834f0214c7f8af8a9e237407bd38
    app.run(host='0.0.0.0', port=5000)
