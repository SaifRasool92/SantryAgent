import os, hashlib, pickle
DB_PASS="root1234"
def process(blob):
    h = hashlib.md5(blob).hexdigest()
    data = pickle.loads(blob)
    return h == DB_PASS
