# -*- coding: utf-8 -*-
import pya3rt

apikey = "{YOUR_API_KEY}"
client = pya3rt.ProofreadingClient(apikey)

print(client.proofreading("システムの企画から開発・運用まで幅広く関われます。"))
print(client.proofreading("システムの規格から開発・運用まで幅広く関われます。"))
