import unittest

import gocardless
from gocardless.client import Client


class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.account_details = {
            'app_id': 'id01',
            'app_secret': 'sec01',
            'token': 'tok01',
            'merchant_id': 'MERCH01',
        }
        self.client = Client(**self.account_details)

    def test_base_url_returns_the_correct_url_for_production(self):
      gocardless.environment = 'production'
      self.assertEqual(Client.get_base_url(), 'https://gocardless.com')

    def test_base_url_returns_the_correct_url_for_sandbox(self):
      gocardless.environment = 'sandbox'
      self.assertEqual(Client.get_base_url(), 'https://sandbox.gocardless.com')

    def test_base_url_returns_the_correct_url_when_set_manually(self):
      Client.base_url = 'https://abc.gocardless.com'
      self.assertEqual(Client.get_base_url(), 'https://abc.gocardless.com')

    def test_app_id_required(self):
        self.account_details.pop('app_id')
        with self.assertRaises(ValueError):
            Client(**self.account_details)

    def test_app_secret_required(self):
        self.account_details.pop('app_secret')
        with self.assertRaises(ValueError):
            Client(**self.account_details)
            
    def test_merchant_request_returns_merchant_details(self):
        """Test that the correct number of values are returned.
        """
        dan_test = {
            'app_id': 'XXXX',
            'app_secret': 'XXXXX',
            'token': 'XXXXXXX',
            'merchant_id': 'XXXXXXX',
        
        }
        Client.base_url = 'https://sandbox.gocardless.com'
        gocardless.environment = 'sandbox'
        dan_client = Client(**dan_test)
        merchant_details = dan_client.merchant()
        self.assertEqual(len(merchant_details.keys()), 13)
        

