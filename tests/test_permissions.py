import unittest
from permissions import can_export
class PermissionTests(unittest.TestCase):
    def test_known_role(self): self.assertTrue(can_export("analyst",True))
    def test_cross_tenant(self): self.assertFalse(can_export("owner",False))
    def test_unknown_role(self): self.assertFalse(can_export("guest",True))
