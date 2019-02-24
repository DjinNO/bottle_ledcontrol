import socket 
from bottle import route, run, template, HTTPResponse, request, get, post, static_file

sock = socket.socket()
sock.connect(('localhost', 9999))

@route('/')
def start_page():
    return template ('start_page')

@route('/random')
def hello():
    sock.send('random\n;render\n'.encode())
    return template ('start_page')

@route('/off')
def hello():
    sock.send('fill 1,000000\n;render\n'.encode())
    return template ('start_page')

@get('/fill')
def fill():
    color = request.query.color
    start = request.query.start
    len = request.query.len
    brightness = request.query.brightness
    sock.send(('fill 1,{0},{1},{2}\n;render\n'.format(color,start,len)).encode())
    sock.send(('brightness 1,{0},{1},{2}\n;render\n'.format(brightness,start,len)).encode())



@post('/send')
def process():
    color = request.forms.get('color')
    start = request.forms.get('start')
    len = request.forms.get('len')
    brightness = request.forms.get('brightness')
    sock.send(('fill 1,{0},{1},{2}\n;render\n'.format(color,start,len)).encode())
    sock.send(('brightness 1,{0},{1},{2}\n;render\n'.format(brightness,start,len)).encode())
    return "Color: {0}  Start: {1} Len: {2} Brightness= {3}".format(color, start, len, brightness)
run(host='0.0.0.0', port=8080, debug=True)


