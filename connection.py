import os
import json
import psycopg2
import hdfs

from sqlalchemy import create_engine

def config(connection_db):
    path = os.getcwd()
    with open(path+'/'+'config.json') as file:
        conf =json.load(file)[connection_db]
    return conf

def psql_conn(conf, name_conn):
    try:
        conn = psycopg2.connect(
            host=conf['host'],
            database=conf['db'],
            user=conf['user'],
            password=conf['password'],
            port=conf['port']
        )
        print(f'[INFO] Success connect PostgreSQL {name_conn}')
        engine = create_engine(f"postgresql+psycopg2://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['db']}")
        return conn, engine
    except Exception as e:
        print(f"[INFO] Can't connect PostgreSQL {name_conn}")
        print(str(e))

def hadoop_conn(conf):
    client = conf['client']
    if 'user.name' in conf:
        conf['user.name'] = conf['user.name'].replace(' ', '_')
    try:
        conn = hdfs.InsecureClient(client, user=conf.get('user.name'))
        print(f"[Info] sucsess connect to HADOOP..")
        return conn
    except Exception as e:
        print(f'[info] cant connect to HADOOP.. ')
        print(str(e))
