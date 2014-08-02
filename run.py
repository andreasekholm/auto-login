#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
Very basic auth for wifi portal.

Written by: https://github.com/andreasekholm

Thanks to: https://github.com/bouncynudibranch

TODO:
    * Retrying after x amount of time
    * Force login page to extend lease
    * If that doesn't work, call for relog after set amount of time
"""

import requests
import sys
import os
from PyQt4 import QtGui, QtCore

url = 'http://192.168.3.1:8000/?redirurl=http%3A%2F%2Fwww.google.com'
data = {
        'auth_user': 'cartel',
        'auth_pass': 'cartel',
        'redirurl': 'http://www.google.com',
        'accept': 'Continue'
        }

def try_auth(url, data):
    r = requests.post(url, data=data)
    return r.status_code


class LoginQt(QtGui.QMainWindow):
    def __init__(self):
        super(LoginQt, self).__init__()
        self.initUI()

    def initUI(self):
        button = QtGui.QPushButton('Login to Cartel', self)
        button.setToolTip('Just push and enjoy free WiFi')
        button.resize(button.sizeHint())
        button.clicked.connect(try_auth)


def main():
    app = QtGui.QApplication(sys.argv)
    ulf = LoginQt()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
