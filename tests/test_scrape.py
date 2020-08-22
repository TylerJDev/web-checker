import unittest
from main import grabItemRequest

class TestMyScraper(unittest.TestCase):
    def test_equalToTwo(self):
        page = 'https://trjones.dev/'
        self.assertEqual(grabItemRequest(page, 'tagName', 'h1'), 'Hello, my name is Tyler')


