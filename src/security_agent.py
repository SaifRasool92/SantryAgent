import json
import subprocess
import os

class SecurityAgent:
    def __init__(self, target_file):
        self.target_file = target_file

    def run_scan(self, output_json_path):
        os.makedirs(os.path.dirname(output_json_path), exist_ok=True)
        cmd = ["bandit", "-f", "json", "-o", output_json_path, self.target_file]
        
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if not os.path.exists(output_json_path):
            return {"total_issues": 0, "severity_counts": {"HIGH": 0, "MEDIUM": 0, "LOW": 0}}

        with open(output_json_path, "r") as f:
            report = json.load(f)

        severity_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
        for result in report.get("results", []):
            sev = result.get("issue_severity", "LOW")
            severity_counts[sev] = severity_counts.get(sev, 0) + 1

        return {
            "total_issues": len(report.get("results", [])),
            "severity_counts": severity_counts,
            "raw_report": report
        }