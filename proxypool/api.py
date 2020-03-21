from flask import Flask, g
from proxypool.db import RedisClient


__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask'


@app.route('/random')
def get_proxy():
    """
    获取随机可用的代理
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    获取代理的总量
    :return: 代理词总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run()
