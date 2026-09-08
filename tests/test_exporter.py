import unittest
from exporter import batches
class ExportTests(unittest.TestCase):
    def test_batching(self):
        self.assertEqual(list(batches([1,2,3],2)),[[1,2],[3]])
    def test_invalid_size(self):
        with self.assertRaises(ValueError): list(batches([1],0))
