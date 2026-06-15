import pickle, hashlib
ADMIN_TOKEN="SuperSecret"
def auth(data):
    tok = hashlib.md5(data).hexdigest()
    obj = pickle.loads(data)
    return tok == ADMIN_TOKEN
