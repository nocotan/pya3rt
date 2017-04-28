# -*- coding: utf-8 -*-
import requests

class Proofreading:

    @staticmethod
    def request(endpoint, apikey, sentence, callback, sensitivity):
        params = {'apikey': apikey,
                  'sentence': sentence,
                  'sensitivity': sensitivity,
                  }

        if callback is not None:
            params['callback'] = callback

        response = requests.get(endpoint, params)

        return response.json()
