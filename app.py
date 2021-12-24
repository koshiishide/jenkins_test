#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
<<<<<<< HEAD
    return 'Lets chanbara!', 200
=======
    return 'Let us chanbara!!!', 200
>>>>>>> a1dafd112940cce400a34b991b0bb6603be28edf


if __name__ == '__main__':
    app.run(debug=True)
