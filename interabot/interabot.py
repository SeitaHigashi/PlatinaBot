# -*- coding: utf-8 -*-

import datetime
import sys
import os

GreetingDict = {'mooning': [4, 5, 6, 7, 8, 9],
                'noon': [10, 11, 12, 13, 14, 15, 16, 17, 18],
                'night': [19, 21, 22, 23, 24, 0, 1, 2, 3]}

class Bot:
    def __init__(self):
        pass

    def Response(self, text):
        if '今何時' in text:
            now = datetime.datetime.now()
            comment = '{}:{:02}だよ！'.format(now.hour, now.minute)
        elif '' in text:
            now = datetime.datetime.now()

        return comment