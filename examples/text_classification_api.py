# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.TextClassificationClient(apikey)

print(client.classify("システムの企画から開発・運用まで幅広く関われます。"))
