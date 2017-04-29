# pya3rt

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)  

pya3rt is an API wrapper for A3RT in Python.

## A3RT
https://a3rt.recruit-tech.co.jp/  
A3RT (art) is an abbreviation for "ANALYTICS & ARTIFICIAL INTELLIGENCE API VIA RECRUIT TECHNOLOGIES".A3RT is a collective name for solutions that are projected to unify and maintain the logic of fields called artificial intelligence, which is represented by Deep Learning and others, among machinery learning, to the inside of the company.

## API

* Text Suggest API
* Text Classification API
* Listing API
* Image Influence API
* Proofreading API
* Talk API

## Install

```
$ pip install pya3rt
```

## examples

### Text Suggest

Text Suggest API is an API that automatically generates text and input assistance born using deep learning technology.

```python
# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.TextSuggestClient(apikey)

print(client.text_suggest("馬"))
print(client.text_suggest("あき", style=1))
print(client.text_suggest("func", style=2))
```

### Text Classification

```python
# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.TextClassificationClient(apikey)

print(client.classify("システムの企画から開発・運用まで幅広く関われます。"))
```

### Proofreading API

```python
# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.ProofreadingClient(apikey)

print(client.proofreading("システムの企画から開発・運用まで幅広く関われます。"))
print(client.proofreading("システムの規格から開発・運用まで幅広く関われます。"))
```

### Image Influence API

```python
# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.ImageInfluenceClient(apikey)

print(client.get_upload_url())
print(client.meat_score("meat1.jpeg", 1))
```

### Talk API

```python
# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.TalkClient(apikey)

print(client.talk("おはよう"))
```
