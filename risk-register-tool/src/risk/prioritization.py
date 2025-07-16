from .models import Risk
from .assessment import calculate_risk_score

def prioritize_risks(risks: list) -> list:
    """
    Prioritize risks based on their severity and exposure.

    Parameters:
    risks (list): A list of risk objects to be prioritized.

    Returns:
    list: A sorted list of risks based on priority.
    """
    return sorted(risks, key=calculate_risk_score, reverse=True)

def allocate_resources(prioritized_risks, available_resources):
    """
    Allocate resources to prioritized risks.

    Parameters:
    prioritized_risks (list): A list of prioritized risk objects.
    available_resources (int): The total resources available for allocation.

    Returns:
    dict: A mapping of risk IDs to allocated resources.
    """
    allocation = {}
    for risk in prioritized_risks:
        if available_resources <= 0:
            break
        allocation[risk.id] = min(risk.required_resources, available_resources)
        available_resources -= allocation[risk.id]
    return allocation

def generate_priority_report(prioritized_risks):
    """
    Generate a report of prioritized risks.

    Parameters:
    prioritized_risks (list): A list of prioritized risk objects.

    Returns:
    str: A formatted report of prioritized risks.
    """
    report_lines = []
    for risk in prioritized_risks:
        score = calculate_risk_score(risk)
        report_lines.append(
            f"Risk ID: {risk.id}, Title: {risk.title}, Category: {risk.category}, "
            f"Likelihood: {risk.likelihood}, Impact: {risk.impact}, Score: {score}, Status: {risk.status}"
        )
    return "\n".join(report_lines)