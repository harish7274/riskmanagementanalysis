from .models import Risk

def calculate_risk_score(risk: Risk) -> int:
    return risk.likelihood * risk.impact

def assess_risk(risk: Risk) -> str:
    score = calculate_risk_score(risk)
    if score >= 16:
        return "High"
    elif score >= 9:
        return "Medium"
    else:
        return "Low"