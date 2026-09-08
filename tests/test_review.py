import unittest
from release_review import review
class ReviewTests(unittest.TestCase):
    def test_done_without_merge(self):
        self.assertEqual(review({"checklist":"done","pr_state":"open"})[0],"MISMATCH")
    def test_blocker(self):
        self.assertEqual(review({"blocker":True,"pr_state":"open"})[0],"BLOCKER")
    def test_merge_is_not_deployment(self):
        code,note=review({"pr_state":"merged"})
        self.assertEqual(code,"MERGED")
        self.assertIn("separate evidence",note)
    def test_no_evidence(self):
        self.assertEqual(review({})[0],"UNKNOWN")
if __name__ == "__main__": unittest.main()
