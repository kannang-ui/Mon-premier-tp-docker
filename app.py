from flask import Flask
import os
import redis

app = Flask(__name__)
cache = redis.Redis(
    host= os.environ.get('REDIS_HOST' , 'db') , 
    port=6379,
    password=os.environ.get('REDIS_PASSWORD'),
    decode_responses=True
    )

@app.route('/')
def hello_world():
    count = cache.incr('hits')
    return f'Salut ! cette page a été vue {count} fois.\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
