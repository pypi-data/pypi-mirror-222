import functools
from . import sql_support
from .engine import Engine
from .init_import import import_driver
from .log_support import logger, insert_log, save_log, get_log, sql_log
from .support import DBCtx, ConnectionCtx, Dict, MultiColumnsError, TransactionCtx, try_commit, DBError, DB_LOCK
from .constant import MYSQL_CONNECTOR_DRIVER, SQLITE, PARAM_DRIVER, PARAM_SHOW_SQL, PARAM_TRANS_PLACEHOLDER, PARAM_DEBUG, PARAM_POOL_SIZE, PARAM_PORT,\
    MYSQL, POSTGRESQL, UNKNOW, MYSQL_PORT, POSTGRESQL_PORT

_DB_CTX = None


def init_db(*args, **kwargs):
    """
    Compliant with the Python DB API 2.0 (PEP-249).

    from sqlexec
    sqlexec.init_db('test.db', driver='sqlite3', show_sql=True, debug=True)
    or
    sqlexec.init_db("postgres://user:password@127.0.0.1:5432/testdb", driver='psycopg2', pool_size=5, show_sql=True, debug=True)
    or
    sqlexec.init_db(user='root', password='xxx', host='127.0.0.1', port=3306, database='testdb', driver='pymysql', pool_size=5, show_sql=True, debug=True)

    Addition parameters:
    :param driver=None: str, import driver, 'import pymysql'
    :param pool_size=0: int, default 0, size of connection pool
    :param show_sql=False: bool,  if True, print sql
    :param debug=False: bool, if True, print debug context
    :param trans_placeholder=True: bool, if True, sql placeholder '?' --> '%s'

    Other parameters of connection pool refer to DBUtils: https://webwareforpython.github.io/DBUtils/main.html#pooleddb-pooled-db
    """

    global _DB_CTX
    pool_size = 0
    driver = kwargs.pop(PARAM_DRIVER) if PARAM_DRIVER in kwargs else None
    show_sql = kwargs.pop(PARAM_SHOW_SQL) if PARAM_SHOW_SQL in kwargs else False
    trans_placeholder = kwargs.pop(PARAM_TRANS_PLACEHOLDER) if PARAM_TRANS_PLACEHOLDER in kwargs else True

    curr_engine = Engine.current_engine()
    if driver is None and (curr_engine is None or curr_engine == UNKNOW) and PARAM_PORT in kwargs:
        port = kwargs[PARAM_PORT]
        if port == MYSQL_PORT:
            curr_engine = MYSQL
        elif port == POSTGRESQL_PORT:
            curr_engine = POSTGRESQL

    engine, driver, creator = import_driver(driver, curr_engine)
    prepared = MYSQL_CONNECTOR_DRIVER == driver
    if PARAM_DEBUG in kwargs and kwargs.pop(PARAM_DEBUG):
        from logging import DEBUG
        logger.setLevel(DEBUG)

    if PARAM_POOL_SIZE in kwargs:
        if prepared:
            # mysql.connector 用自带连接池
            pool_size = kwargs[PARAM_POOL_SIZE]
        else:
            pool_size = kwargs.pop(PARAM_POOL_SIZE)

    pool_args = ['mincached', 'maxcached', 'maxshared', 'maxconnections', 'blocking', 'maxusage', 'setsession', 'reset', 'failures', 'ping']
    pool_kwargs = {key: kwargs.pop(key) for key in pool_args if key in kwargs}
    connect = lambda: creator.connect(*args, **kwargs)
    if pool_size >= 1 and not prepared:
        from .pooling import pooled_connect
        connect = pooled_connect(connect, pool_size, **pool_kwargs)

    with DB_LOCK:
        if _DB_CTX is not None:
            raise DBError('DB is already initialized.')
        _DB_CTX = DBCtx(connect=connect, prepared=prepared)

    if SQLITE == engine:
        trans_placeholder = False
    Engine.init0(engine, trans_placeholder, show_sql)
    if pool_size > 0:
        logger.info("Inited db engine <%s> of %s with driver: '%s' and pool size: %d." % (hex(id(_DB_CTX)), engine, driver, pool_size))
    else:
        logger.info("Inited db engine <%s> of %s with driver: '%s'." % (hex(id(_DB_CTX)), engine, driver))


def connection():
    """
    Return _ConnectionCtx object that can be used by 'with' statement:
    with connection():
        pass
    """
    global _DB_CTX
    return ConnectionCtx(_DB_CTX)


def with_connection(func):
    """
    Decorator for reuse connection.
    @with_connection
    def foo(*args, **kw):
        f1()
        f2()
    """

    global _DB_CTX
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        with ConnectionCtx(_DB_CTX):
            return func(*args, **kw)
    return _wrapper


def transaction():
    """
    Create a transaction object so can use with statement:
    with transaction():
        pass
    with transaction():
         insert(...)
         update(... )
    """
    global _DB_CTX
    return TransactionCtx(_DB_CTX)


def with_transaction(func):
    """
    A decorator that makes function around transaction.
    @with_transaction
    def update_profile(id, name, rollback):
         u = dict(id=id, name=name, email='%s@test.org' % name, passwd=name, last_modified=time.time())
         insert('person', **u)
         r = update('update person set passwd=? where id=?', name.upper(), id)
    """
    global _DB_CTX
    @functools.wraps(func)
    def _wrapper(*args, **kw):
        with TransactionCtx(_DB_CTX):
            return func(*args, **kw)
    return _wrapper


@with_connection
def execute(sql: str, *args):
    """
    Execute sql return effect rowcount
    sql: insert into person(name, age) values(?, ?)  -->  args: ('张三', 20)
    """
    global _DB_CTX
    cursor = None
    sql = Engine.before_execute_intf('execute', sql.strip(), *args)
    try:
        cursor = _DB_CTX.connection.cursor()
        cursor.execute(sql, args)
        effect_rowcount = cursor.rowcount
        try_commit(_DB_CTX)
        return effect_rowcount
    finally:
        if cursor:
            cursor.close()


def insert(table: str, **kwargs):
    """
    Insert data into table, return effect rowcount.
    :param table: table name
    :param kwargs: name='张三', age=20}
    return: Effect rowcount
    """
    insert_log('insert', table, **kwargs)
    sql, args = sql_support.insert_sql_args(table.strip(), **kwargs)
    return execute(sql, *args)


def save(select_key: str, table: str, **kwargs):
    """
    Insert data into table, return primary key.
    :param select_key: sql for select primary key
    :param table: table
    :param kwargs:
    :return: Primary key
    """
    save_log('save', select_key, table, **kwargs)
    sql, args = sql_support.insert_sql_args(table.strip(), **kwargs)
    return save_sql(select_key, sql, *args)


def save_sql(select_key: str, sql: str, *args, **kwargs):
    """
    Insert data into table, return primary key.
    :param select_key: sql for select primary key
    :param sql: table
    :param args:
    :return: Primary key
    """
    logger.debug("Exec func 'sqlexec.%s', 'select_key': %s \n\t sql: %s \n\t args: %s \n\t kwargs: %s" % ('save_sql', select_key, sql, args, kwargs))
    sql, args = sql_support.get_mapping_sql_args(sql, *args, **kwargs)
    return do_save_sql(select_key, sql, *args)


def batch_insert(table: str, *args):
    """
    Batch insert
    :param table: table name
    :param args: All number must have same key. [{'name': '张三', 'age': 20}, {'name': '李四', 'age': 28}]
    :return: Effect row count
    """
    logger.debug("Exec func 'sqlexec.%s' \n\t Table: '%s', args: %s" % ('batch_insert', table, args))
    assert len(args) > 0, 'args should not be empty.'
    sql, args = sql_support.batch_insert_sql_args(table, *args)
    return batch_execute(sql, *args)


@with_connection
def batch_execute(sql: str, *args):
    """
    Batch execute sql return effect rowcount
    :param sql: insert into person(name, age) values(?, ?)  -->  args: [('张三', 20), ('李四', 28)]
    :param args: All number must have same size.
    :return: Effect rowcount
    """
    global _DB_CTX
    cursor = None
    if isinstance(args[0], dict):
        sql, args = sql_support.batch_named_sql_args(sql, *args)
    sql = Engine.before_execute_intf('batch_execute', sql.strip(), *args)
    args = sql_support.get_batch_args(*args)
    try:
        cursor = _DB_CTX.cursor()
        cursor.executemany(sql, args)
        effect_rowcount = cursor.rowcount
        try_commit(_DB_CTX)
        return effect_rowcount
    finally:
        if cursor:
            cursor.close()


def get(sql: str, *args, **kwargs):
    """
    Execute select SQL and expected one int and only one int result, SQL contain 'limit'.
    MultiColumnsError: Expect only one column.
    sql: SELECT count(1) FROM person WHERE name=? and age=? limit 1  -->  args: ('张三', 20)
    """
    sql, args = _try_mapping('sqlexec.get', sql, *args, **kwargs)
    return do_get(sql, *args)


def select(sql: str, *args, **kwargs):
    """
    execute select SQL and return unique result or list results(tuple).
    sql: SELECT * FROM person WHERE name=? and age=?  -->  args: ('张三', 20)
    """
    sql, args = _try_mapping('sqlexec.select', sql, *args, **kwargs)
    return do_select(sql, *args)


def select_one(sql: str, *args, **kwargs):
    """
    Execute select SQL and return unique result(tuple), SQL contain 'limit'.
    sql: SELECT * FROM person WHERE name=? and age=? limit 1  -->  args: ('张三', 20)
    """
    sql, args = _try_mapping('sqlexec.select_one', sql, *args, **kwargs)
    return do_select_one(sql, *args)


def query(sql: str, *args, **kwargs):
    """
    Execute select SQL and return list results(dict).
    sql: SELECT * FROM person WHERE name=? and age=?  -->  args: ('张三', 20)
    """
    sql, args = _try_mapping('sqlexec.query', sql, *args, **kwargs)
    return do_query(sql, *args)


def query_one(sql: str, *args, **kwargs):
    """
    execute select SQL and return unique result(dict), SQL contain 'limit'.
    sql: SELECT * FROM person WHERE name=? and age=? limit 1  -->  args: ('张三', 20)
    """
    sql, args = _try_mapping('sqlexec.query_one', sql, *args, **kwargs)
    return do_query_one(sql, *args)


@with_connection
def do_execute(sql: str, *args):
    """
    Execute sql return effect rowcount
    sql: insert into person(name, age) values(?, ?)  -->  args: ('张三', 20)
    """
    global _DB_CTX
    cursor = None
    sql = Engine.before_execute_intf('do_execute', sql.strip(), *args)
    try:
        cursor = _DB_CTX.connection.cursor()
        cursor.execute(sql, args)
        effect_rowcount = cursor.rowcount
        try_commit(_DB_CTX)
        return effect_rowcount
    finally:
        if cursor:
            cursor.close()


@with_connection
def do_save_sql(select_key: str, sql: str, *args):
    """
    Insert data into table, return primary key.
    :param select_key: sql for select primary key
    :param sql: table
    :param args:
    :return: Primary key
    """
    global _DB_CTX
    cursor = None
    logger.debug("Exec func 'sqlexec.%s', 'select_key': %s" % ('do_save_sql', select_key))
    sql = Engine.before_execute_intf('save_sql', sql, *args)
    try:
        cursor = _DB_CTX.connection.cursor()
        cursor.execute(sql, args)
        cursor.execute(select_key)
        result = cursor.fetchone()
        try_commit(_DB_CTX)
        return result[0]
    finally:
        if cursor:
            cursor.close()


def do_get(sql: str, *args):
    """
    Execute select SQL and expected one int and only one int result, SQL contain 'limit'.
    MultiColumnsError: Expect only one column.
    sql: SELECT count(1) FROM person WHERE name=? and age=? limit 1  -->  args: ('张三', 20)
    """
    get_log('get', sql, *args)
    result = select_one(sql, *args)
    if result:
        if len(result) == 1:
            return result[0]
        msg = "Exec func 'sqlexec.%s' expect only one column but %d." % ('do_get', len(result))
        logger.error('%s  \n\t sql: %s \n\t args: %s' % (msg, sql, args))
        raise MultiColumnsError(msg)
    return None


@with_connection
def do_select(sql: str, *args):
    """
    execute select SQL and return unique result or list results(tuple).
    sql: SELECT * FROM person WHERE name=? and age=?  -->  args: ('张三', 20)
    """
    global _DB_CTX
    cursor = None
    sql = Engine.before_execute_intf('do_select', sql.strip(), *args)
    try:
        cursor = _DB_CTX.cursor()
        cursor.execute(sql, args)
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()


@with_connection
def do_select_one(sql: str, *args):
    """
    Execute select SQL and return unique result(tuple), SQL contain 'limit'.
    sql: SELECT * FROM person WHERE name=? and age=? limit 1  -->  args: ('张三', 20)
    """
    global _DB_CTX
    cursor = None
    sql = Engine.before_execute_intf('do_select_one', sql.strip(), *args)
    try:
        cursor = _DB_CTX.cursor()
        cursor.execute(sql, args)
        return cursor.fetchone()
    finally:
        if cursor:
            cursor.close()


@with_connection
def do_query(sql: str, *args):
    """
    Execute select SQL and return list results(dict).
    sql: SELECT * FROM person WHERE name=? and age=?  -->  args: ('张三', 20)
    """
    global _DB_CTX
    cursor = None
    sql = Engine.before_execute_intf('do_query', sql.strip(), *args)
    try:
        cursor = _DB_CTX.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
        if results and cursor.description:
            names = list(map(lambda x: x[0], cursor.description))
            return list(map(lambda x: Dict(names, x), results))
        else:
            return results
    finally:
        if cursor:
            cursor.close()


@with_connection
def do_query_one(sql: str, *args):
    """
    execute select SQL and return unique result(dict), SQL contain 'limit'.
    sql: SELECT * FROM person WHERE name=? and age=? limit 1  -->  args: ('张三', 20)
    """
    global _DB_CTX
    cursor = None
    sql = Engine.before_execute_intf('do_query_one', sql.strip(), *args)
    try:
        cursor = _DB_CTX.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        if result and cursor.description:
            names = [x[0] for x in cursor.description]
            return Dict(names, result)
        return result
    finally:
        if cursor:
            cursor.close()


def get_connection():
    global _DB_CTX
    _DB_CTX.try_init()
    return _DB_CTX.connection


def _try_mapping(function, sql, *args, **kwargs):
    sql_log(function, sql, *args, **kwargs)
    return sql_support.get_mapping_sql_args(sql, *args, **kwargs)
