# -*- coding: utf-8 -*-
import requests

class TextSuggest:

    @staticmethod
    def request(endpoint, apikey, previous_description, callback, style, separation):
        params = {'apikey': apikey,
                  'previous_description': previous_description,
                  'style': style,
                  'separation': separation,
                  }

        if callback is not None:
            params['callback'] = callback

        response = requests.get(endpoint, params)

        return response.json()
