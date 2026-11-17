# Phishing Risk Analyzer

A beginner-friendly Python program that asks six Yes/No questions about a
suspicious email and reports a **low**, **medium**, or **high** phishing risk.

## Run it

Make sure Python 3 is installed, then run:

```bash
python3 phishing_risk_analyzer.py
```

Answer each question with `yes` or `no`. The program counts the warning signs:

- 0–1 warning signs: **LOW RISK**
- 2–3 warning signs: **MEDIUM RISK**
- 4 or more warning signs: **HIGH RISK**

The result includes the score, risk level, detected warning signs, and a
recommendation. You can choose to analyze another message when it finishes.
The score is only a guide: when an email seems suspicious, do not click links
or open attachments. Verify the message using a trusted way to contact the
supposed sender.
