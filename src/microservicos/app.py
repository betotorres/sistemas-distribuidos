from flask import Flask
import json
from flask import current_app, g
import sqlite3


app = Flask(__name__)

DATABASE = 'dados/banco_1.db'



def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    results = [tuple(row) for row in rv]
    cur.close()

    #return (rv[0] if rv else None) if one else rv
    return json.dumps(results)

def update_db(query, args=(), one=False):
    try:
        cur = get_db().execute(query, args)
        get_db().commit()
        cur.close()
        return True
    except Exception as e:
        print(e)
        return False
        


@app.route("/contas", methods=['GET'])
def retorna_contas():
    return query_db('select * from contas')


@app.route('/conta/<cpf>', methods=['GET'])
def get_saldo(cpf):
    return query_db("select saldo from contas where cpf == ?", (cpf,))


@app.route('/debito/<cpf>/<valor>', methods=['GET'])
def efetua_debito(cpf, valor):
    print(cpf, valor)
    retorno = update_db("update contas set saldo = saldo - ? where cpf = ?", (valor, cpf,))
    if retorno:
        return '1'
    else:
        return '0'


@app.route('/credito/<cpf>/<valor>', methods=['GET'])
def efetua_credito(cpf, valor):
    print(cpf, valor)
    retorno = update_db("update contas set saldo = saldo + ? where cpf = ?", (valor, cpf,))
    if retorno:
        return '1'
    else:
        return '0'



@app.route('/conta/<cpf>', methods=['GET'])
def get_user(cpf):

    return query_db("select * from contas where cpf = '?", cpf)

