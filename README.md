# SentryAgent v2 — ML-Driven Secure Code Refactoring & Risk Prediction

SentryAgent v2 combines machine learning vulnerability risk prediction (`RandomForestClassifier`), static security analysis (`bandit`), and automated refactoring/verification agents.

## Architecture & Workflow

1. **Synthetic Dataset Generation**: Constructs 15 unique Python files representing varied software complexity levels.
2. **ML Risk Model (`src/risk_model.py`)**: Computes line count, AST cyclomatic complexity (via `radon`), and security keyword counts to predict vulnerable code risk.
3. **Bandit Static Scan**: Conducts initial vulnerabilities scan.
4. **Refactoring Agent**: Rewrites target codebase to address AST security issues.
5. **Verifier Agent**: Validates syntax compilation and execution runtime.

## Running the Pipeline

```bash
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/6c613129-516e-4fdd-980e-1d17051a976f" />

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/da6fcfdb-9f1c-42a9-a361-0b42b16bff0a" />
