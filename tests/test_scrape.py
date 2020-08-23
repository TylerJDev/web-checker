import unittest
from main import grabItemRequest

class TestMyScraper(unittest.TestCase):
    def setUp(self): 
        self.def_page = 'https://tylerjdev.github.io/web-checker/'
    
    def test_equalToTagNameText(self):
        self.assertEqual(grabItemRequest(self.def_page, 'tagName', 'h1'), 'Hello, World!')

    def test_equalToIDNameText(self):
        self.assertEqual(grabItemRequest(self.def_page, 'id', 'test_id'), 'Hello, World, too!')
        
    def test_equalToClassNameText(self):
        self.assertEqual(grabItemRequest(self.def_page, 'className', 'test_class'), 'Drive in, drive in!')

