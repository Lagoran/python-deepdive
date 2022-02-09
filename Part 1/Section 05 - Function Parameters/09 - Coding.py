from datetime import datetime

def log(msg, *, dt = None):
    dt = dt or datetime.utcnow()
    print("{0} - {1}".format(msg,dt))

log('test')
log('test', dt = '2022-1-1 12:15:59.0000000')
