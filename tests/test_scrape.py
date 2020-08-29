import unittest
from main import grabItemRequest, itemChangeCheck


class TestMyScraper(unittest.TestCase):
    def setUp(self): 
        self.def_page = 'https://tylerjdev.github.io/web-checker/'
    
    def test_equalToTagNameText(self):
        self.assertEqual(grabItemRequest(self.def_page, 'tagName', 'h1').text, 'Hello, World!')

    def test_equalToIDNameText(self):
        self.assertEqual(grabItemRequest(self.def_page, 'id', 'test_id').text, 'Hello, World, too!')
        
    def test_equalToClassNameText(self):
        self.assertEqual(grabItemRequest(self.def_page, 'className', 'test_class').text, 'Drive in, drive in!')

    def test_itemChangeCheck(self):
        item_1 = grabItemRequest(self.def_page, 'id', 'test_random')
        item_2 = grabItemRequest(self.def_page, 'id', 'test_random')
        self.assertFalse(itemChangeCheck(item_1, ''))
        self.assertFalse(itemChangeCheck(item_1, item_2))

