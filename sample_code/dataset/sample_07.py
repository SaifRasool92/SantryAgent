import hashlib
def hash_pass(p):
    return hashlib.md5(p.encode()).hexdigest()
