import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors
POOL = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=1,
    maxcached=1,
    maxshared=1,
    blocking=True,
    maxusage=None,
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='a3022535842',
    db='kimoServer',
    charset='utf8'
)

def fetch_one(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor(cursor = cursors.DictCursor)
    cursor.execute(sql,params)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def register_user(sql,params):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql,params)
    result = conn.commit()
    cursor.close()
    conn.close()
    return result

def fetchall(sql):
    conn = POOL.connection()
    cursor = conn.cursor(cursor=cursors.DictCursor)
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result