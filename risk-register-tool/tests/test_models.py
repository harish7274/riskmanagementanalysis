from src.risk.models import Risk, Threat, Control
from src.risk.mitigation import add_mitigation
import unittest

class TestRiskModels(unittest.TestCase):

    def setUp(self):
        self.risk = Risk(
            id=1,
            title="Data Breach",
            description="Unauthorized access to sensitive data",
            category="Data",
            likelihood=4,
            impact=5
        )
        self.threat = Threat(name="Malicious attempt", description="Malicious attempt to access data", likelihood=0.8)
        self.control = Control(name="Firewall", description="Blocks unauthorized access", effectiveness=0.85)

    def test_risk_initialization(self):
        self.assertEqual(self.risk.description, "Unauthorized access to sensitive data")
        self.assertEqual(self.risk.likelihood, 4)
        self.assertEqual(self.risk.impact, 5)
        add_mitigation(self.risk, "Encryption", "Security Team")
        self.assertEqual(self.risk.mitigations[0].action, "Encryption")

    def test_threat_initialization(self):
        self.assertEqual(self.threat.description, "Malicious attempt to access data")
        self.assertEqual(self.threat.likelihood, 0.8)

    def test_control_initialization(self):
        self.assertEqual(self.control.description, "Blocks unauthorized access")
        self.assertEqual(self.control.effectiveness, 0.85)

if __name__ == '__main__':
    unittest.main()