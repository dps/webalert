import json
import requests
import redis
import sys

class DemoListener(object):

    def __init__(self):
        pass

    def hit(self):
        print "Hit!"


class WebAlert(object):

    def __init__(self, token, listener):
        jd = json.JSONDecoder()
        self._token = token
        self._listener = listener
        creds = jd.decode(requests.get('http://webalert.davidsingleton.org/creds').text)
        self._redis = redis.StrictRedis(host=creds['host'], port=creds['port'],
            db=0, password=creds['password'])

    def loop(self):
        pubsub = self._redis.pubsub()
        pubsub.subscribe(self._token)
        for event in pubsub.listen():
            if event["type"] == "message":
                self._listener.hit()


if __name__ == '__main__':
    listener = DemoListener()
    w = WebAlert(sys.argv[1], listener)
    w.loop()
