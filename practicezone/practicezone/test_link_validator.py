import re
from django.test import Client
import unittest
from django.core.management import call_command
from django.contrib.auth.models import AnonymousUser

import sys
import os

# Disable


def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore


def enablePrint():
    sys.stdout = sys.__stdout__


class LinkTest(unittest.TestCase):
    def __init__(self):
        self.client = Client()
        # self.ok_url = []
        # self.notok_url = []
        self.my_url_without_var_list = []
        self.link_test_result = []
        blockPrint()
        raw_url_list = call_command('show_urls').split('\n')
        enablePrint()
        raw_url_list.remove('')
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        for raw_url in raw_url_list:
            url = ansi_escape.sub('', raw_url.split('\t')[0])
            is_without_var = not all(test in url for test in ['<', '>'])
            if is_without_var:
                self.my_url_without_var_list.append(url)
        self.my_url_without_var_list.remove('/test')

    def test_url_without_var(self):
        for test_url in self.my_url_without_var_list:
            response = self.client.get(test_url)
            try:
                self.assertIs(response.status_code in (200, 301, 302), True)
                self.link_test_result.append([test_url, response.status_code])
            except AssertionError as e:
                self.link_test_result.append((e, response.status_code))
                continue
        return self.link_test_result
