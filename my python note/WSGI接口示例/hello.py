#-*- coding:utf8 -*-

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>我是你的好朋友</h1>'
