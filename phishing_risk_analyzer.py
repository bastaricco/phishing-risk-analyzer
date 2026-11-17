"""A beginner-friendly phishing risk checker."""


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
    if score >= 5:
        return "high"
    if score >= 3:
        return "medium"
    return "low"


def assess_email():
    """Ask about common warning signs and return the risk rating."""
    print("Phishing Risk Analyzer")
    print("Answer a few questions about the suspicious email.")

    questions = [
        ("Did the email ask you to click a link?", 2),
        ("Did it ask for a password, payment, or other personal information?", 3),
        ("Does it create a strong sense of urgency or threaten you?", 2),
        ("Is the sender unfamiliar or does the address look unusual?", 2),
        ("Does it contain an unexpected attachment?", 2),
    ]

    score = 0
    for question, points in questions:
        if ask_yes_no(question):
            score += points

    rating = get_risk_rating(score)
    print(f"\nPhishing risk: {rating.upper()}")
    if rating == "high":
        print("Do not click links, open attachments, or reply. Report the email.")
    elif rating == "medium":
        print("Be careful. Verify the sender another way before taking action.")
    else:
        print("No major warning signs were found, but stay cautious.")
    return rating


if __name__ == "__main__":
    assess_email()
