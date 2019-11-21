from webtest import TestApp
# from boddle import boddle
import kafka_selfservice

# def test_webapp_index():
#   with boddle(params={'name': 'Derek'}):
#     assert kafka_selfservice.index() == 'Hi Derek!'

def test_webapp_ping():
  app = TestApp(kafka_selfservice.app)
  assert app.get('/v1/ping').status == '200 OK'
