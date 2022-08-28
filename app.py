import time

import redis
from flask import Flask

app = Flask(__name__) #irá criar um nome para o flask
cache = redis.Redis(host='redis', port=6379) #define a porta padrão do redis(serviço de estrutura de dados)

def get_hit_count(): #esta fazendo uma contagem
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/') #criando um diretório princial no flask
def hello():
    count = get_hit_count()
    return 'Olá pessoal! Atualize para mudar. Já está em {}.\n'.format(count)

