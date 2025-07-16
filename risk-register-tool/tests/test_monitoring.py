import unittest
from src.risk.models import Risk
from src.risk.monitoring import update_risk_status, get_open_risks

class TestRiskMonitoring(unittest.TestCase):
    def setUp(self):
        self.risk1 = Risk(id=1, title="A", description="", category="", likelihood=2, impact=2)
        self.risk2 = Risk(id=2, title="B", description="", category="", likelihood=3, impact=3, status="Mitigated")
        self.risks = [self.risk1, self.risk2]

    def test_update_risk_status(self):
        update_risk_status(self.risk1, "Closed")
        self.assertEqual(self.risk1.status, "Closed")

    def test_get_open_risks(self):
        open_risks = get_open_risks(self.risks)
        self.assertEqual(len(open_risks), 1)
        self.assertEqual(open_risks[0].title, "A")

    def test_alert_for_open_risks(self):
        open_risks = get_open_risks(self.risks)
        for risk in open_risks:
            print(f"Monitoring Alert: Risk '{risk.title}' is still open!")
        self.assertTrue(any(risk.status == "Open" for risk in open_risks))

if __name__ == '__main__':
    unittest.main()