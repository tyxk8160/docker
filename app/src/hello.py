

from flask import Flask, render_template,request
from flask_bootstrap import Bootstrap
import redis
import urllib
import pdb
rds=redis.StrictRedis('db', 6379)


app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    #pdb.set_trace()

    ip = request.__dict__['environ']['REMOTE_ADDR']
    realip = request.__dict__['environ']['REMOTE_ADDR']

    rds.incr('index', 1)
    cnt = rds.get('index')
    cnt = 0 if cnt is None else cnt
    
    return render_template('index.html',cnt=cnt,ip = ip)


@app.route('/user/<name>')
def user(name):
    rds.incr(name , 1)
    cnt = rds.get(name)
    cnt = 0 if cnt is None else cnt
    return render_template('user.html', name=name,cnt=cnt)



if __name__ == '__main__':
    app.run(host='0.0.0.0')