import py_compile
import subprocess

class VerifierAgent:
    def __init__(self, target_file):
        self.target_file = target_file

    def verify_syntax(self):
        try:
            py_compile.compile(self.target_file, doraise=True)
            return True, "Syntax valid."
        except Exception as e:
            return False, f"Syntax Error: {str(e)}"

    def verify_execution(self):
        try:
            res = subprocess.run(["python3", self.target_file], capture_output=True, text=True, timeout=5)
            if res.returncode == 0:
                return True, "Execution verified."
            return False, f"Runtime Error: {res.stderr}"
        except Exception as e:
            return False, f"Execution Exception: {str(e)}"