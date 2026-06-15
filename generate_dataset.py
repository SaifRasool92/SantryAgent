import os

def generate_samples():
    os.makedirs("sample_code/dataset", exist_ok=True)
    
    samples = [
        # Clean Files (0 Vulnerabilities)
        ("sample_01.py", 'def add(a, b):\n    return a + b\n'),
        ("sample_02.py", 'import json\ndef parse_data(raw):\n    return json.loads(raw)\n'),
        ("sample_03.py", 'import os\ndef get_env_var(key):\n    return os.getenv(key, "default")\n'),
        ("sample_04.py", 'def calculate_factorial(n):\n    if n == 0: return 1\n    return n * calculate_factorial(n-1)\n'),
        ("sample_05.py", 'import logging\ndef log_info(msg):\n    logging.info(msg)\n'),
        
        # Low/Medium Risk Files (1-2 Vulnerabilities)
        ("sample_06.py", 'import subprocess\ndef run_ls(dir_path):\n    return subprocess.Popen(f"ls {dir_path}", shell=True)\n'),
        ("sample_07.py", 'import hashlib\ndef hash_pass(p):\n    return hashlib.md5(p.encode()).hexdigest()\n'),
        ("sample_08.py", 'import socket\ndef open_port():\n    s = socket.socket()\n    s.bind(("0.0.0.0", 8080))\n'),
        ("sample_09.py", 'PASSWORD = "HardcodedSecret123"\ndef check(p):\n    return p == PASSWORD\n'),
        ("sample_10.py", 'import pickle\ndef load_data(raw_bytes):\n    return pickle.loads(raw_bytes)\n'),
        
        # High Risk Files (3+ Vulnerabilities)
        ("sample_11.py", 'import os, subprocess, hashlib\nKEY="12345"\ndef run(cmd):\n    h = hashlib.md5(cmd.encode())\n    s = subprocess.Popen(cmd, shell=True)\n    return h\n'),
        ("sample_12.py", 'import socket, subprocess\nHOST="0.0.0.0"\ndef start():\n    s = socket.socket()\n    s.bind((HOST, 9090))\n    subprocess.run("rm -rf /tmp/*", shell=True)\n'),
        ("sample_13.py", 'import pickle, hashlib\nADMIN_TOKEN="SuperSecret"\ndef auth(data):\n    tok = hashlib.md5(data).hexdigest()\n    obj = pickle.loads(data)\n    return tok == ADMIN_TOKEN\n'),
        ("sample_14.py", 'import subprocess, socket\nSECRET="API_KEY_9999"\ndef exec_server():\n    s = socket.socket()\n    s.bind(("0.0.0.0", 5000))\n    subprocess.Popen("echo " + SECRET, shell=True)\n'),
        ("sample_15.py", 'import os, hashlib, pickle\nDB_PASS="root1234"\ndef process(blob):\n    h = hashlib.md5(blob).hexdigest()\n    data = pickle.loads(blob)\n    return h == DB_PASS\n')
    ]
    
    for filename, code in samples:
        path = os.path.join("sample_code/dataset", filename)
        with open(path, "w") as f:
            f.write(code)

if __name__ == "__main__":
    generate_samples()