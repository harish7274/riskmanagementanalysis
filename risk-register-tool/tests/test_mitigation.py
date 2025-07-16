import unittest
from src.risk.models import Risk
from src.risk.mitigation import add_mitigation

class TestRiskMitigation(unittest.TestCase):
    def setUp(self):
        self.risk = Risk(id=1, title="Phishing Attack", description="Risk of credential theft via phishing", category="Social Engineering", likelihood=4, impact=5)

    def test_add_single_mitigation(self):
        add_mitigation(self.risk, "Conduct phishing awareness training", "Security Team")
        self.assertEqual(len(self.risk.mitigations), 1)
        self.assertEqual(self.risk.mitigations[0].action, "Conduct phishing awareness training")
        self.assertEqual(self.risk.mitigations[0].owner, "Security Team")
        self.assertEqual(self.risk.mitigations[0].status, "Planned")

    def test_add_multiple_mitigations(self):
        add_mitigation(self.risk, "Enable email filtering", "IT")
        add_mitigation(self.risk, "Implement MFA", "IT Security")
        self.assertEqual(len(self.risk.mitigations), 2)
        actions = [m.action for m in self.risk.mitigations]
        self.assertIn("Enable email filtering", actions)
        self.assertIn("Implement MFA", actions)

    def test_mitigation_status_update(self):
        add_mitigation(self.risk, "Deploy anti-phishing tool", "IT")
        self.risk.mitigations[0].status = "In Progress"
        self.assertEqual(self.risk.mitigations[0].status, "In Progress")
        self.risk.mitigations[0].status = "Complete"
        self.assertEqual(self.risk.mitigations[0].status, "Complete")

    def test_no_mitigation(self):
        empty_risk = Risk(id=2, title="Zero-Day Exploit", description="Unknown vulnerability", category="Malware", likelihood=5, impact=5)
        self.assertEqual(len(empty_risk.mitigations), 0)

    def test_access_control(self):
        add_mitigation(self.risk, "Enable MFA", "IT Security")
        # Simulate access granted if mitigation is complete
        self.risk.mitigations[0].status = "Complete"
        access = "Granted" if self.risk.mitigations[0].status == "Complete" else "Denied"
        print(f"Mitigation: Access {access}")
        self.assertEqual(access, "Granted")

    def test_access_denied(self):
        add_mitigation(self.risk, "Enable MFA", "IT Security")
        # Simulate access denied if mitigation is not complete
        access = "Granted" if self.risk.mitigations[0].status == "Complete" else "Denied"
        print(f"Mitigation: Access {access}")
        self.assertEqual(access, "Denied")

if __name__ == '__main__':
    unittest.main()