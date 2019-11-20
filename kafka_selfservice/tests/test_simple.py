import kafka_selfservice
from boddle import boddle

def test_webapp_index():
  with boddle(params={'name': 'Derek'}):
    assert kafka_selfservice.index() == 'Hi Derek!'
