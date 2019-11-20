from bottle import request, route, run, template

@route('/')
def index():
    return 'Hi %s!' % request.params['name']

run(host='localhost', port=8080, debug=True)
