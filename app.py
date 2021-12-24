#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
<<<<<<< HEAD
    return 'nyanya!', 200







if __name__ == '__main__':
    app.run(debug=True)
