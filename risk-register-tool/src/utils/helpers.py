def log_message(message):
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def validate_risk_data(risk_data):
    """Validates the risk data to ensure required fields are present."""
    required_fields = ['name', 'description', 'likelihood', 'impact']
    for field in required_fields:
        if field not in risk_data:
            log_message(f"Validation Error: '{field}' is required.")
            return False
    return True

def calculate_risk_score(likelihood, impact):
    """Calculates the risk score based on likelihood and impact."""
    return likelihood * impact

def format_risk_report(risk):
    """Formats a risk report for display."""
    return f"Risk: {risk['name']}\nDescription: {risk['description']}\nLikelihood: {risk['likelihood']}\nImpact: {risk['impact']}\nScore: {calculate_risk_score(risk['likelihood'], risk['impact'])}"