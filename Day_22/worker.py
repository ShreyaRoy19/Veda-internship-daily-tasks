import redis
from rq import Worker, Queue, Connection

# Tell RQ which queue(s) to listen to
listen = ['default']

conn = redis.Redis(host='localhost', port=6379, db=0)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
