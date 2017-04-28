# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.TalkClient(apikey)

print(client.talk("おはよう"))

