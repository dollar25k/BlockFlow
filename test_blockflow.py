# test_blockflow.py
"""
Tests for BlockFlow module.
"""

import unittest
from blockflow import BlockFlow

class TestBlockFlow(unittest.TestCase):
    """Test cases for BlockFlow class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockFlow()
        self.assertIsInstance(instance, BlockFlow)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockFlow()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
