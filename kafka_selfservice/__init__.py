from bottle import Bottle, request, route, run, template, get
import kafka_selfservice

app = Bottle()
@app.get('/v1/ping')
def ping():
    return('pong')



app.run(host='localhost', port=8080, debug=True)
