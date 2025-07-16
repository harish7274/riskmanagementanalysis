# Configuration settings for the risk register tool

class Config:
    """Configuration settings for the risk register tool."""
    
    # Application settings
    APP_NAME = "Risk Register Tool"
    APP_VERSION = "1.0.0"
    
    # Risk management parameters
    RISK_LIKELIHOOD_SCALE = {
        "Rare": 1,
        "Unlikely": 2,
        "Possible": 3,
        "Likely": 4,
        "Almost Certain": 5
    }
    
    RISK_IMPACT_SCALE = {
        "Insignificant": 1,
        "Minor": 2,
        "Moderate": 3,
        "Major": 4,
        "Catastrophic": 5
    }
    
    # Thresholds for risk prioritization
    RISK_PRIORITY_THRESHOLD = 10  # Example threshold for prioritization
    
    # Monitoring settings
    MONITORING_INTERVAL = 30  # in minutes
    ALERT_THRESHOLD = 5  # Number of alerts before escalation
    
    # Logging settings
    LOGGING_LEVEL = "INFO"
    LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"