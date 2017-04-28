# -*- coding: utf-8 -*-
import requests

class ImageInfluence:

    @staticmethod
    def meat_score(endpoint, apikey, imagefile, predict):
        params = {'apikey': apikey,
                  'predict': predict,
                  }
        files = {'imagefile': open(imagefile, 'rb')}
        response = requests.post(endpoint, params, files=files)

        return response.json()

    @staticmethod
    def image_score(endpoint, apikey, imagefile, predict):
        params = {'apikey': apikey,
                  'predict': predict,
                  }
        files = {'imagefile': open(imagefile, 'rb')}
        response = requests.post(endpoint, params, files=files)

        return response.json()

    @staticmethod
    def get_upload_url(endpoint, apikey):
        params = {'apikey': apikey}
        response = requests.get(endpoint, params)
        return response.json()

    @staticmethod
    def order_model(endpoint, apikey):
        params = {'apikey': apikey}
        response = requests.get(endpoint, params)
        return response.json()

    @staticmethod
    def status_model(endpoint, apikey):
        params = {'apikey': apikey}
        response = requests.get(endpoint, params)
        return response.json()
