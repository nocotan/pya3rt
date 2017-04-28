# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.ImageInfluenceClient(apikey)

print(client.get_upload_url())
print(client.meat_score("meat1.jpeg", 1))

