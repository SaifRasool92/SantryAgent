import os
import glob
import pandas as pd
import numpy as np
from radon.complexity import cc_visit
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from src.security_agent import SecurityAgent

class VulnerabilityRiskModel:
    def __init__(self, dataset_dir="sample_code/dataset"):
        self.dataset_dir = dataset_dir
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self.features_df = None

    def extract_features(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        lines = len(code.splitlines())
        
        try:
            blocks = cc_visit(code)
            avg_cc = np.mean([b.complexity for b in blocks]) if blocks else 1.0
        except Exception:
            avg_cc = 1.0

        risky_keywords = ["shell=True", "md5", "0.0.0.0", "pickle.loads", "PASSWORD", "SECRET", "TOKEN"]
        keyword_count = sum(code.count(kw) for kw in risky_keywords)

        return [lines, avg_cc, keyword_count]

    def build_dataset(self):
        files = glob.glob(os.path.join(self.dataset_dir, "*.py"))
        data = []

        for fpath in files:
            feats = self.extract_features(fpath)
            
            sec_agent = SecurityAgent(fpath)
            report = sec_agent.run_scan("results/temp_scan.json")
            total_issues = report["total_issues"]
            
            label = 1 if total_issues >= 2 else 0
            data.append(feats + [total_issues, label])

        if os.path.exists("results/temp_scan.json"):
            os.remove("results/temp_scan.json")

        self.features_df = pd.DataFrame(data, columns=["line_count", "avg_complexity", "risky_keywords", "bandit_issues", "is_high_risk"])
        return self.features_df

    def train_and_evaluate(self):
        if self.features_df is None:
            self.build_dataset()

        X = self.features_df[["line_count", "avg_complexity", "risky_keywords"]]
        y = self.features_df["is_high_risk"]

        self.model.fit(X, y)
        preds = self.model.predict(X)

        metrics = {
            "accuracy": accuracy_score(y, preds),
            "precision": precision_score(y, preds, zero_division=0),
            "recall": recall_score(y, preds, zero_division=0),
            "f1": f1_score(y, preds, zero_division=0)
        }

        cm = confusion_matrix(y, preds)
        plt.figure(figsize=(5, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Low Risk', 'High Risk'], yticklabels=['Low Risk', 'High Risk'])
        plt.title('Vulnerability Risk Model Confusion Matrix')
        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')
        plt.tight_layout()
        os.makedirs("results/charts", exist_ok=True)
        plt.savefig("results/charts/risk_model_confusion_matrix.png")
        plt.close()

        return metrics

    def predict_file_risk(self, filepath):
        feats = np.array([self.extract_features(filepath)])
        prob = self.model.predict_proba(feats)[0][1]
        pred = self.model.predict(feats)[0]
        return pred, prob