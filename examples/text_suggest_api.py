# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.TextSuggestClient(apikey)

print(client.text_suggest("馬"))
print(client.text_suggest("あき", style=1))
print(client.text_suggest("func", style=2))

