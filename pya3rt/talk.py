# -*- coding: utf-8 -*-
import requests

class Talk:

    @staticmethod
    def request(endpoint, apikey, query, callback):
        params = {'apikey': apikey,
                  'query': query,
                  }
        if callback is not None:
            params['callback'] = callback

        response = requests.post(endpoint, params)

        return response.json()

