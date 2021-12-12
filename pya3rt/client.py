# -*- coding: utf-8 -*-
from .text_suggest import TextSuggest
from .text_classification import TextClassification
from .proofreading import Proofreading
from .talk import Talk
from .image_influence import ImageInfluence
from .listing import Listing

ENDPOINTS = {
    'text_suggest': 'https://api.a3rt.recruit.co.jp/text_suggest/v2/predict',
    'text_classification': {
        'classify': 'https://api.a3rt.recruit.co.jp/text_classification/v1/classify',
        'dataset': 'https://api.a3rt.recruit.co.jp/text_classification/v1/dataset',
        'model': 'https://api.a3rt.recruit.co.jp/text_classification/v1/model',
        'check_status': 'https://api.a3rt.recruit.co.jp/text_classification/v1/check_status',
    },
    'listing': {
        'get_upload_url': 'https://api.a3rt.recruit.co.jp/listing/v1/get_upload_url',
        'start_w2v': 'https://api.a3rt.recruit.co.jp/listing/v1/start_w2v',
        'status_w2v': 'https://api.a3rt.recruit.co.jp/listing/v1/status_w2v',
        'get_download_url': 'https://api.a3rt.recruit.co.jp/listing/v1/get_download_url',
        'cancel_w2v': 'https://api.a3rt.recruit.co.jp/listing/v1/cancel_w2v',
    },
    'proofreading': 'https://api.a3rt.recruit.co.jp/proofreading/v2/typo',
    'talk': 'https://api.a3rt.recruit.co.jp/talk/v1/smalltalk',
}


class TextSuggestClient(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.endpoint = ENDPOINTS['text_suggest']

    def text_suggest(self, previous_description, callback=None, style=0, separation=2):
        endpoint = self.endpoint
        apikey = self.apikey
        return TextSuggest.request(endpoint, apikey, previous_description,
                                   callback, style, separation)


class TextClassificationClient(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.endpoint = ENDPOINTS['text_classification']

    def classify(self, text, model_id='default'):
        endpoint = self.endpoint['classify']
        apikey = self.apikey
        return TextClassification.classify(endpoint, apikey, text, model_id)

    def dataset(self):
        endpoint = self.endpoint['dataset']
        apikey = self.apikey
        return TextClassification.dataset(endpoint, apikey)

    def model(self, dataset_id):
        endpoint = self.endpoint['model']
        apikey = self.apikey
        return TextClassification.model(endpoint, apikey, dataset_id)

    def model_status(self, model_id):
        endpoint = self.endpoint['model_status']
        apikey = self.apikey
        return TextClassification.model_status(endpoint, apikey, model_id)


class ListingClient(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.endpoint = ENDPOINTS['listing']

    def get_upload_url(self, payload):
        endpoint = self.endpoint['get_upload_url']
        apikey = self.apikey
        return Listing.get_upload_url(endpoint, apikey, payload)

    def start_w2v(self, payload):
        endpoint = self.endpoint['start_w2v']
        apikey = self.apikey
        return Listing.start_w2v(endpoint, apikey, payload)

    def status_w2v(self, payload):
        endpoint = self.endpoint['status_w2v']
        apikey = self.apikey
        return Listing.status_w2v(endpoint, apikey, payload)

    def get_download_url(self, payload):
        endpoint = self.endpoint['get_download_url']
        apikey = self.apikey
        return Listing.get_download_url(endpoint, apikey, payload)

    def cancel_w2v(self, payload):
        endpoint = self.endpoint['cancel_w2v']
        apikey = self.apikey
        return Listing.cancel_w2v(endpoint, apikey, payload)


class ProofreadingClient(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.endpoint = ENDPOINTS['proofreading']

    def proofreading(self, sentence, callback=None, sensitivity='medium'):
        endpoint = self.endpoint
        apikey = self.apikey
        return Proofreading.request(endpoint, apikey, sentence, callback, sensitivity)


class TalkClient(object):

    def __init__(self, apikey):
        self.apikey = apikey
        self.endpoint = ENDPOINTS['talk']

    def talk(self, query, callback=None):
        endpoint = self.endpoint
        apikey = self.apikey
        return Talk.request(endpoint, apikey, query, callback)
