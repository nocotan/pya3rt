# -*- coding: utf-8 -*-
import requests

class TextClassification:

    @staticmethod
    def classify(endpoint, apikey, text, model_id):
        params = {'apikey': apikey,
                  'text': text,
                  'model_id': model_id,
                  }

        response = requests.post(endpoint, params)

        return response.json()

    @staticmethod
    def dataset(endpoint, apikey):
        params = {'apikey': apikey}
        response = requests.post(endpoint, params)
        return response.json()

    @staticmethod
    def model(endpoint, apikey, dataset_id):
        params = {'apikey': apikey,
                  'dataset_id': dataset_id,
                  }
        response = requests.post(endpoint, params)

        return response.json()

    @staticmethod
    def model_status(endpoint, apikey, model_id):
        params = {'apikey': apikey,
                  'model_id': model_id,
                  }
        response = requests.post(endpoint, params)

        return response.json()
