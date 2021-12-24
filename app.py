#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
<<<<<<< HEAD
    return 'Hello,world!', 200
=======
<<<<<<< HEAD
    return 'See you, Joy!', 200
=======
    return 'Hello, Joy Wu!', 200
>>>>>>> f7e1d3b13e0eb2b5595e8426eab203541169cbb4
>>>>>>> 291d6e3262b690212e6b3bf3aa084db4071184ec

if __name__ == '__main__':
    app.run(debug=True)
