# -*- coding: utf-8 -*-
import requests

class Listing:

    @staticmethod
    def get_upload_url(endpoint, apikey, payload):
        params = {'apikey': apikey,
                  'payload': payload,
                  }

        response = requests.get(endpoint, params)
        return response.json()

    @staticmethod
    def start_w2v(endpoint, apikey, payload):
        params = {'apikey': apikey,
                  'payload': payload,
                  }
        response = requests.get(endpoint, params)
        return response.json()

    @staticmethod
    def status_w2v(endpoint, apikey, payload):
        params = {'apikey': apikey,
                  'payload': payload,
                  }
        response = requests.get(endpoint, params)
        return response.json()

    @staticmethod
    def get_download_url(endpoint, apikey, payload):
        params = {'apikey': apikey,
                  'payload': payload,
                  }
        response = requests.get(endpoint, params)
        return response.json()

    @staticmethod
    def cancel_w2v(endpoint, apikey, payload):
        params = {'apikey': apikey,
                  'payload': payload,
                  }
        response = requests.get(endpoint, params)
        return response.json()

