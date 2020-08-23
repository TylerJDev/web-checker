import unittest
from main import grabItemRequest

class TestMyScraper(unittest.TestCase):
    def test_equalToTwo(self):
        page = 'https://tylerjdev.github.io/web-checker/'
        self.assertEqual(grabItemRequest(page, 'tagName', 'h1'), 'Hello, World!')


