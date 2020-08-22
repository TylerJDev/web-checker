import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from main import grabItemRequest

class TestMyScraper(unittest.TestCase):
    def test_equalToTwo(self):
        page = 'https://trjones.dev/'
        self.assertEqual(grabItemRequest(page), 'Hello, my name is Tyler')


