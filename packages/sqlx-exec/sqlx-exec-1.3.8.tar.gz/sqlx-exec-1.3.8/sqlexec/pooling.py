from sqlexec.support import DB_LOCK

_POOL = None
MAX_POOL_SIZE = 32

def pooled_connect(creator, pool_size, **kwargs):
    global _POOL
    assert 1 <= pool_size <= MAX_POOL_SIZE, 'pool_size should be higher or equal to 1 and lower or equal to {}'.format(MAX_POOL_SIZE)
    if _POOL is None:
        mincached = kwargs['mincached'] if 'mincached' in kwargs else pool_size
        maxcached = kwargs['maxcached'] if 'maxcached' in kwargs else pool_size
        maxconnections = kwargs['maxconnections'] if 'maxconnections' in kwargs else MAX_POOL_SIZE
        with DB_LOCK:
            if _POOL is None:
                from dbutils.pooled_db import PooledDB
                # kwargs['creator'] = creator
                # kwargs['mincached'] = mincached
                # kwargs['maxcached'] = maxcached
                # kwargs['maxshared'] = 0
                # kwargs['maxconnections'] = maxconnections
                # kwargs['blocking'] = False
                # kwargs['maxusage'] = None
                # kwargs['setsession'] = None
                # kwargs['reset'] = True
                # kwargs['failures'] = None
                # kwargs['ping'] = 1
                # _POOL = PooledDB(dsn, **kwargs)
                # _POOL = PooledDB(creator, mincached, maxcached, 0, maxconnections, False, None, None, True, None, 1)
                _POOL = PooledDB(creator, mincached=mincached, maxcached=maxcached, maxconnections=maxconnections)
    return _POOL.connection

