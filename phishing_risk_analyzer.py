"""A beginner-friendly phishing risk checker."""


WARNING_SIGN_QUESTIONS = [
    ("Unexpected message", "Was this message unexpected?"),
    ("Unknown or suspicious sender", "Is the sender unknown or suspicious?"),
    ("Urgent or threatening language", "Does it use urgent or threatening language?"),
    (
        "Request for sensitive information",
        "Does it request a password, credit card number, or other sensitive information?",
    ),
    ("Suspicious or misleading link", "Does it contain a suspicious or misleading link?"),
    ("Unexpected attachment", "Does it contain an unexpected attachment?"),
]


def ask_yes_no(question):
    """Ask a question until the user enters yes or no."""
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Please answer yes or no.")


def get_risk_rating(score):
    """Convert a phishing warning score into a simple risk rating."""
    if score >= 4:
        return "high"
    if score >= 2:
        return "medium"
    return "low"


def assess_email():
    """Ask about common warning signs and return the risk rating."""
    print("Phishing Risk Analyzer")
    print("Answer a few questions about the suspicious email.\n")

    detected_warning_signs = []
    for warning_sign, question in WARNING_SIGN_QUESTIONS:
        if ask_yes_no(question):
            detected_warning_signs.append(warning_sign)

    risk_score = len(detected_warning_signs)
    risk_level = get_risk_rating(risk_score)
    print("\n--- Analysis result ---")
    print(f"Risk score: {risk_score}/{len(WARNING_SIGN_QUESTIONS)}")
    print(f"Risk level: {risk_level.upper()}")
    print("Warning signs detected:")
    if detected_warning_signs:
        for warning_sign in detected_warning_signs:
            print(f"- {warning_sign}")
    else:
        print("- None")

    print("\nRecommendation:")
    rating = risk_level
    if rating == "high":
        print("Do not click links, open attachments, or reply. Report the email.")
    elif rating == "medium":
        print("Be careful. Verify the sender another way before taking action.")
    else:
        print("No major warning signs were found, but stay cautious.")
    return risk_score, risk_level, detected_warning_signs


def main():
    """Analyze messages until the user chooses to stop."""
    while True:
        assess_email()
        if not ask_yes_no("\nWould you like to analyze another message?"):
            print("Stay safe online!")
            break


if __name__ == "__main__":
    main()
