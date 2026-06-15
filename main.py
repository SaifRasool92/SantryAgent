import os
import matplotlib.pyplot as plt
from generate_dataset import generate_samples
from src.security_agent import SecurityAgent
from src.refactor_agent import RefactorAgent
from src.verifier_agent import VerifierAgent
from src.risk_model import VulnerabilityRiskModel

def main():
    print("....SentryAgent v2 Pipeline Started....")
    
    print("\n1. Generating Multi-File Code Dataset (15 Samples)...")
    generate_samples()
    print("   Dataset generated in sample_code/dataset/")

    print("\n2. Training ML Risk Model (Random Forest)...")
    risk_model = VulnerabilityRiskModel()
    metrics = risk_model.train_and_evaluate()
    print("   ML Risk Model Performance:")
    print(f"   -> Accuracy:  {metrics['accuracy']:.4f}")
    print(f"   -> Precision: {metrics['precision']:.4f}")
    print(f"   -> Recall:    {metrics['recall']:.4f}")
    print(f"   -> F1-Score:  {metrics['f1']:.4f}")

    before_file = "sample_code/before/vulnerable_app.py"
    after_file = "sample_code/after/refactored_app.py"
    report_before_path = "results/security_report_before.json"
    report_after_path = "results/security_report_after.json"
    chart_path = "results/charts/vulnerability_reduction.png"

    print("\n3. Predicting Risk on Target App using ML Model...")
    is_risk, prob = risk_model.predict_file_risk(before_file)
    print(f"   Target: {before_file}")
    print(f"   ML Predicted High Risk: {bool(is_risk)} (Probability: {prob:.2%})")

    print("\n4. Running Initial Security Scan (Bandit)...")
    sec_agent_before = SecurityAgent(before_file)
    before_metrics = sec_agent_before.run_scan(report_before_path)
    print(f"   Before Refactoring -> Total Issues: {before_metrics['total_issues']} | Breakdown: {before_metrics['severity_counts']}")

    print("\n5. Executing Autonomous Refactoring Agent...")
    refactor_agent = RefactorAgent(before_file)
    refactor_agent.refactor(after_file)
    print(f"   Refactored code written to: {after_file}")

    print("\n6. Verifying Refactored Code Functional Integrity...")
    verifier = VerifierAgent(after_file)
    syntax_ok, syntax_msg = verifier.verify_syntax()
    exec_ok, exec_msg = verifier.verify_execution()
    print(f"   Syntax Check: {syntax_msg}")
    print(f"   Runtime Check: {exec_msg}")

    print("\n7. Running Post-Refactoring Security & ML Risk Scan...")
    sec_agent_after = SecurityAgent(after_file)
    after_metrics = sec_agent_after.run_scan(report_after_path)
    _, post_prob = risk_model.predict_file_risk(after_file)
    print(f"   After Refactoring  -> Total Issues: {after_metrics['total_issues']} | Breakdown: {after_metrics['severity_counts']}")
    print(f"   Post-Refactor ML Risk Probability: {post_prob:.2%}")

    print("\n8. Generating Comparison Visuals...")
    os.makedirs("results/charts", exist_ok=True)
    
    severities = ["HIGH", "MEDIUM", "LOW"]
    before_counts = [before_metrics['severity_counts'].get(s, 0) for s in severities]
    after_counts = [after_metrics['severity_counts'].get(s, 0) for s in severities]

    x = range(len(severities))
    width = 0.35

    plt.figure(figsize=(7, 5))
    plt.bar([p - width/2 for p in x], before_counts, width, label='Before Refactoring', color='#d9534f')
    plt.bar([p + width/2 for p in x], after_counts, width, label='After Refactoring', color='#5cb85c')
    
    plt.xlabel('Vulnerability Severity')
    plt.ylabel('Issue Count')
    plt.title('Bandit Static Analysis: Vulnerability Remediation')
    plt.xticks(x, severities)
    plt.legend()
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    print(f"   Chart saved to: {chart_path}")
    print("\n....SentryAgent v2 Pipeline Completed Successfully....")

if __name__ == "__main__":
    main()