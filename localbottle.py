#-*- coding:utf-8 -*-
#localhost testing
#caroltc 2014/10/7
from bottle import route, run, request
from smallgfw import *
import json
import hashlib
import sys
import shutil
import tempfile
import os

file_words = 'words.txt' 
gfw = GFW(file_words)

@route('/replace', method="POST")
def replace():
    getwords = request.params.words or ""
    res = gfw.check(getwords.encode('utf8'))
#    for obj in res:
#        print json.dumps(obj),obj[2]
    s = gfw.replace(getwords.encode('utf8'),"**")
    return s

@route('/check',method="POST")
def check():
    res = gfw.check(request.body.read())
    resp = {}
    resp['count'] = len(res)
    resp['datas']= res
    return json.dumps(resp)

@route('/test')
def test():
    webdata = '<h1>check</h1><form action="/replace" method="post"><input type="text" name="words" /><input type="submit"></from>'
    return webdata

@route('/update/<time:re:[0-9]+>/<sign:re:[a-zA-Z0-9_]+>',method="POST")
def update(time, sign):
    if hashlib.md5((time+"replace with your key")).hexdigest() == sign:
        file_bak = "_"+file_words
        shutil.copy(file_words, file_bak)
        fp = open(file_words,'w')
        fp.write(request.body.read())  
        fp.close()
        os.unlink(file_bak)
        return "success"
    return "fail"

run(host='localhost', port=80, debug=True)