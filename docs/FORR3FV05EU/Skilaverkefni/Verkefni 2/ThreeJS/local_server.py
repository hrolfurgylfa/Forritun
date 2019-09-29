#TIL KENNARA!!!
#       |
#       |
#       V
#Til þess að finna Verkefni 1 þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_1 og til þess að finna verkefni tvö þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_2

import json
import urllib.request
from sys import argv

import bottle
from bottle import *

@route("/")
def main():

    with open('index.html', 'r') as content_file:
        content = content_file.read()

    return content

#  ========================================
#  Annað
#  ========================================
# Til þess að setja inn myndir
@route("/models/<slod:path>")
def static_models(slod):
    return static_file(slod, root="models")

@route("/js/<slod:path>")
def static_js(slod):
    return static_file(slod, root="js")

#404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða
@error(404)
def notFound(error):
    return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'


bottle.run(host="localhost", port=8080, reloader=True, debug=True)
